"""
Machine Learning based approach to find scientific names
NetiNeti uses a trained classifier to find and collect scientific
names from a document
Input: Any text preferably in Engish
Output : A list of scientific names
"""

from netineti.tokenizer import Tokenizer
from netineti.list_data import ListData
from netineti.name_candidate import NameCandidate
from netineti.name_parser import NameParser

class NameFinder(object):
    """Uses the trained NetiNetiTrainer model and searches through text
    to find names.

    This version supports offsets.

    """
    @staticmethod
    def _prepare_output(names):
        return names

    def __init__(self, model):
        """Creates the name finder object.

        Arguments:
        model_object -- a trained NetiNetiTrainer instance object

        """
        self.lists = ListData()
        self._model_object = model
        self._tokens = []
        self.parser = NameParser()

    def find(self, text):
        """
        Takes a text string in UTF-8 encoding, returns a string of names
        concatenated with a newline and a list of offsets for each mention of
        the name in the original text.

        Arguments:
        text -- input text
        """
        self._tokens = Tokenizer(text).tokenize()
        names = self._traverse_tokens()
        return self._prepare_output(names)

    def _traverse_tokens(self):
        """Takes tokens from the end of tokens array,
        evaluates them, and starts searching for names
        from 'promising' tokens"""
        pre_names = self._collect_pre_names()
        self._parse_raw(pre_names)
        import pdb; pdb.set_trace()
        return self._refine_names(pre_names)

    def _collect_pre_names(self):
        """Collects possible names by finding capitalized words and
        assesing them on plausability as genera, also looking for a possible
        species epithet"""
        pre_names = []
        while True:
            pre_name = self._find_next_candidate()
            if pre_name:
                pre_names.append(pre_name)
            else: break
        return pre_names

    def _find_next_candidate(self):
        while self._tokens:
            name_candidate = NameCandidate(self._tokens.pop(), self._tokens)
            if name_candidate.is_promising():
                return name_candidate
        return None

    def _parse_raw(self, pre_names):
        self.parser.start()
        for name in pre_names:
            name.parsed_raw = self.parser.parse(name.string)
        self.parser.stop()


    def _prepare_name_candidate(self, token):
        pass


    def _examine_name_candidate(self, name_candidate):
        pass

    def _refine_names(self, pre_names):
        pass
