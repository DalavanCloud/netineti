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
        from 'promising' tokens

        """
        pre_names = self._collect_pre_names()
        return self._refine_names(pre_names)

    def _collect_pre_names(self):
        pre_names = []
        while self._tokens:
            name_candidate = self._find_next_candidate()
            if name_candidate.contains_name():
                pre_names << name_candidate
        return pre_names

    def _find_next_candidate(self):
        while self._tokens:
            name_candidate = NameCandidate(self._tokens.pop(), self._tokens)
            if name_candidate.is_promising():
                return name_candidate
        return NameCandidate(None, None)

    def _prepare_name_candidate(self, token):
        pass


    def _examine_name_candidate(self, name_candidate):
        pass

