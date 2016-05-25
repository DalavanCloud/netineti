"""Keeps and evaluates data that might contain scientific name"""
from netineti.token import Token

class NameCandidate(object):
    """Keeps and pre-evaluates data that might contain scientific name"""

    def __init__(self, token, tokens):
        self.token = token
        self.tokens = tokens

    def is_promising(self):
        """Evaluates quality of NameCandidate"""

        return isinstance(self.token, Token) and len(self.token.verbatim) > 0

    def contains_name(self):
        pass
