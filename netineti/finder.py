"""
Machine Learning based approach to find scientific names
NetiNeti uses a trained classifier to find and collect scientific
names from a document
Input: Any text preferably in Engish
Output : A list of scientific names
"""
import os
import re
import nltk
import netineti.helper as helper

class NetiNeti(object):
    """Uses the trained NetiNetiTrainer model and searches through text
    to find names.

    This version supports offsets.

    """

    def __init__(self, model_object, black_list_file='data/black/bayes.txt'):
        """Creates the name finder object.

        Arguments:
        model_object -- a trained NetiNetiTrainer instance object
        black_list_file -- file containing black-listed words
          (default "data/black_list.txt")

        """
        black_list = open(os.path.dirname(os.path.realpath(__file__)) + "/"  +
                          black_list_file)
        self._black_list = frozenset([l.rstrip() for l in black_list])
        self._model_object = model_object
        self._text = ''
        self._names_list = []
        self._offsets_list = []
        self._names_dict = {}
        self._index_dict = {}
        self._count = -1

    def find_names(self, text):
        """
        Return a string of names concatenated with a newline and a list of
        offsets for each mention of the name in the original text.

        Arguments:
        text -- input text
        """
        self._text = text
        self._offsets_list = []
        self._names_list = []
        self._index_dict = {}
        self._count = -1
        space_regex = re.compile(r'\s')
        tokens = space_regex.split(text) #any reason not to use nltk tokenizer?

        names_verbatim, offsets = self._find_names_in_tokens(tokens)
        names_set = set(self._names_list)
        names_list = list(names_set)
        names_list.sort()
        return "\n".join(names_list), names_verbatim, offsets

    def _find_names_in_tokens(self, tokens):
        """Returns tuple
        Takes list of all tokens from a document and returns back tuple
        of found names. First element is a an alphabetised list of unique
        names, second -- names in the order of their occurance in the document,
        third --  offsets for each mention of the name in the document

        Arguments:
        tokens -- list with all tokens from the searched document

        """
        self._index_dict = helper.create_index(tokens)
        token_string = " ".join(tokens)

        if len(tokens) == 2:
            if (self._is_like_binomial(tokens[0], tokens[1])
                    and self._is_a_name(token_string, tokens, 0, 1)):
                self._names_list.append(token_string)
        elif len(tokens) == 1:
            if (len(tokens[0]) > 2
                    and tokens[0][0].isupper()
                    and tokens[0].isalpha()
                    and self._is_not_in_black_list(tokens[0])
                    and self._is_a_name(tokens[0], tokens, 0, 0)):
                self._names_list.append(tokens[0])
        else:
            trigrams = list(nltk.trigrams(tokens))
            self._walk_trigrams(trigrams, tokens)
            self._check_last_bigram_unigram(trigrams[-1], tokens)
        return self._generate_output()

    def _generate_output(self):
        """Returns tuple
        Generates offsets for names and returns verbatim version of names as
        they are appearing in the searched document

        """
        names_verbatim = []
        offsets = []
        for offset in self._offsets_list:
            name = self._text[offset[0]:offset[1]]
            parts = name.split(" ")
            if parts[0][0] + parts[0][-1] == "()":
                offset1 = offset[0]
                offset2 = offset[1] + helper.right_strip(name)[1]
            else:
                offset1 = offset[0] + helper.left_strip(name)[1]
                offset2 = offset[1] + helper.right_strip(name)[1]
            name = self._text[offset1:offset2]
            names_verbatim.append(name)
            offsets.append((offset1, offset2))

        return(names_verbatim, offsets)

    def _walk_trigrams(self, trigrams, tokens):
        """Returns None
        Walks over all trigrams and collects found names

        Attributes:
        trigrams - list of trigrams generated from the text
        tokens - one word tokens from the document
        """
        for word1_orig, word2_orig, word3_orig in trigrams:
            self._count += 1
            word1, word2, word3 = helper.clean_token(word1_orig.strip(),
                                                     word2_orig.strip(),
                                                     word3_orig)
            bigram = helper.remove_trailing_period(word1 + " " + word2)
            trigram = helper.remove_trailing_period(word1 + " " + word2 +
                                                    " " + word3)
            if self._is_like_trinomial(word1, word2, word3):
                if self._is_a_name(trigram, tokens, self._count, 2):
                    start, end = self._get_offsets(word1_orig, word2_orig,
                                                   word3_orig)
                    self._offsets_list.append((start, end))
                    self._prepare_name(word1, word2, word3)
            elif self._is_like_binomial(word1, word2):
                if self._is_a_name(bigram, tokens, self._count, 1):
                    start, end = self._get_offsets(word1_orig, word2_orig)
                    self._offsets_list.append((start, end))
                    self._prepare_name(word1, word2, "")
            elif self._is_like_uninomial(word1):
                if self._is_a_name(
                        re.sub(r"\.", ". ",
                               helper.remove_trailing_period(word1)),
                        tokens, self._count, 0):
                    start, end = self._get_offsets(word1_orig)
                    self._offsets_list.append((start, end))
                    self._names_list.append(
                        helper.remove_trailing_period(word1))
                elif helper.has_uninomial_ending(word1):
                    start, end = self._get_offsets(word1_orig)
                    self._offsets_list.append((start, end))
                    self._names_list.append(
                        helper.remove_trailing_period(word1))
            elif helper.has_uninomial_ending(word1):
                if (self._is_not_in_black_list(word1) and word1[0].isupper()
                        and helper.remove_trailing_period(word1).isalpha()):
                    start, end = self._get_offsets(word1_orig)
                    self._offsets_list.append((start, end))
                    self._names_list.append(
                        helper.remove_trailing_period(word1))

    def _check_last_bigram_unigram(self, trigram, tokens):
        """Returns None
        Goes through the last generated trigram to find uninomial or
        bionomial names

        Attributes:
        trigram - a trigram
        tokens - one word tokens generated from the searched document

        """

        bigram = helper.remove_trailing_period(trigram[-2] + " " + trigram[-1])
        unigram = re.sub(r"\. ", " ",
                         helper.remove_trailing_period(trigram[-2]))
        if self._is_like_binomial(trigram[-2], trigram[-1]):
            if self._is_a_name(bigram, tokens, self._count + 1, 1):
                self._prepare_name(trigram[-2], trigram[-1], "")
            elif self._is_like_uninomial(unigram):
                if self._is_a_name(unigram, tokens, self._count + 1, 0):
                    self._names_list.append(unigram)

    def _is_like_uninomial(self, word):
        """Returns a boolean
        Checks if a word looks like a uninomial.

        Arguments:
        word -- a word to check as a ponential uninomial

        """
        # This method currently only allows uninomials of size larger
        # than 5, however there are uninomials which are 2 characters in size.

        is_like_uninomial = (len(word) > 5
                             and word[0].isupper()
                             and word[1:].islower()
                             and (helper.remove_trailing_period(word).isalpha()
                                  or (word[0].isupper() and word[1] == "."
                                      and word[2].islower()
                                      and helper.
                                      remove_trailing_period(word[2:]).
                                      isalpha()))
                             and self._is_not_in_black_list(word))
        return is_like_uninomial

    def _is_like_binomial(self, first_word, second_word):
        """Returns a boolean.
        Checks if a bigram can potentially be a binomial name

        Arguments:
        first_word -- first element of a bigram
        second_word -- second element of a bigram

        """
        if len(first_word) > 1 and len(second_word) > 1:
            is_abbr_word = (first_word[1] == '.' and len(first_word) == 2)
            is_a_candidate = (first_word[0].isupper()
                              and second_word.islower()
                              and ((first_word[1:].islower()
                                    and first_word.isalpha()) or is_abbr_word)
                              and (helper.
                                   remove_trailing_period(second_word).isalpha()
                                   or '-' in second_word))
            return (is_a_candidate
                    and self._is_not_in_black_list(first_word)
                    and self._is_not_in_black_list(second_word))
        else:
            return False

    def _is_like_trinomial(self, first_word, second_word, third_word):
        """Returns a boolean.
        Checks if a trigram looks like a trinomial name

        Arguments:
        first_word -- first element of a trigram
        second_word -- second element of a trigram
        third_word -- third element of a trigram

        """
        if len(first_word) > 1 and len(second_word) > 1 and len(third_word) > 1:
            third_word_ok = (third_word.islower()
                             and helper.remove_trailing_period(third_word).
                             isalpha())

            if second_word[0] + second_word[-1] == "()":
                second_word_ok = (second_word[1].isupper()
                                  and ((second_word[2] == "."
                                        and len(second_word) == 4)
                                       or second_word[2:-1].islower()
                                       and second_word[2:-1].isalpha())
                                  and second_word[-1] != ".")
                return (second_word_ok and third_word_ok
                        and self._is_not_in_black_list(third_word)
                        and (first_word[0].isupper()
                             and ((first_word[1] == "."
                                   and len(first_word) == 2)
                                  or first_word[1:].islower()
                                  and first_word.isalpha())))
            else:
                return (third_word_ok
                        and self._is_like_binomial(first_word, second_word)
                        and self._is_not_in_black_list(third_word))
        elif (len(first_word) > 1
              and len(second_word) == 0
              and len(third_word) > 1):
            return self._is_like_binomial(first_word, third_word)
        else:
            return False

    def _is_not_in_black_list(self, word):
        """Returns a boolean.
        Checks if a word is in a black list

        Arguments:
        word -- a token, first element of a trigram

        """
        word = helper.strip_token(word)
        for w in  word.split("-"):
            if w.lower() in self._black_list:
                return False
        return True

    def _is_a_name(self, token, context, index, span):
        """Returns a boolean
        Checks if a token is a scientific name or not.

        Arguments:
        token -- a name string consisting of 1-3 words
        context -- list of words surrounding the token
        index -- index where the token happens in the document
        span -- length of the token in the document

        """
        features = self._model_object.taxon_features(token, context,
                                                     index, span)
        return self._model_object.get_model().classify(features) == 'taxon'

    def _prepare_name(self, word1, word2, word3):
        """Returns None
        Composes a name from words and adds it to the names list

        Arguments:
        word1 -- the first word of a name
        word2 -- the second word of a name
        word3 -- the third word of a name

        """
        if word2 == "":
            name = helper.remove_trailing_period((word1 + " " + word3).strip())
        else:
            name = helper.remove_trailing_period((word1 + " " + word2 +
                                                  " " + word3).strip())
        if name[1] == "." and name[2] == " ":
            self._names_list.append(name)
        else:
            self._names_list.append(name)
            self._names_dict[helper.remove_trailing_period(
                (word1[0] + ". " + word2 + " " + word3).strip())] = word1[1:]

    def _get_offsets(self, word1, word2='', word3=''):
        """Returns word1 tuple with start and end positions of
        word1 found scientific name.

        Arguments:
        word1 -- first element of word1 trigram
        word2 -- second element of word1 trigram
        word3 -- third element of word1 trigram
        """
        name = word1 + " " + word2 + " " + word3
        name = name.strip()
        return (self._index_dict[self._count],
                self._index_dict[self._count] + len(name))
