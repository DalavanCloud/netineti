"""Token object keeps information about a word in text"""
import re

class Token(object):
    """Implements logic associated with tokens"""

    @staticmethod
    def is_tokenizable(string):
        """Checks if a string should be tokenized"""

        return len(string) > 0


    def __init__(self, start, end, verbatim):
        """Builds Token instance

        Keyword arguments
        start -- index of the first letter
        end -- index of the last letter
        value -- string representation of the word

        """
        self.noalpha = re.compile(u'^[\\W\\d_]*(.*?)[\\W\\d_]*$', re.U | re.M)
        self.start = start
        self.end = end
        self.verbatim = verbatim
        self.cleaned = self.noalpha.match(verbatim).group(1)
