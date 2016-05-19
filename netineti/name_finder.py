"""
Machine Learning based approach to find scientific names
NetiNeti uses a trained classifier to find and collect scientific
names from a document
Input: Any text preferably in Engish
Output : A list of scientific names
"""

import os
from netineti.tokenizer import Tokenizer

class NameFinder(object):
    """Uses the trained NetiNetiTrainer model and searches through text
    to find names.

    This version supports offsets.

    """
    DATA_PATH = os.path.dirname(os.path.realpath(__file__)) + "/data/"

    def __init__(self, model):
        """Creates the name finder object.

        Arguments:
        model_object -- a trained NetiNetiTrainer instance object

        """
        black_list = open(NameFinder.DATA_PATH + 'black_list.txt')
        self._black_list = frozenset([l.rstrip() for l in black_list])
        self._model_object = model
        self._tokens = []

    def find(self, text):
        """
        Return a string of names concatenated with a newline and a list of
        offsets for each mention of the name in the original text.

        Arguments:
        text -- input text
        """
        self._tokens = Tokenizer(text).tokenize()

