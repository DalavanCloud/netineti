"""Keeps and evaluates data that might contain a scientific name"""
import netineti.features as features
from netineti.name_extractor import NameExtractor
from netineti.name_string import NameString

class NameCandidate(object):
    """Keeps and pre-evaluates data that might contain scientific name"""

    def __init__(self, token, tokens):
        self.token = token
        self.offset = token.start
        self.tokens = tokens[0:15][::-1]
        self.name_string = NameString(self.token, self.tokens)
        self.parsed = {}
        self.result = None

    def is_promising(self):
        """Evaluates quality of NameCandidate"""
        w = self.token.verbatim
        is_a_maybe = len(self.token.verbatim) > 0 and features.is_capitalized(w)
        if not is_a_maybe:
            is_a_maybe = features.is_like_hybrid_sign(w)
        return is_a_maybe

    def select(self, with_nlp=False):
        """Selects names candidates which contained scientific names.
        The parsed must be created for this method to work correctly"""
        assert (self.parsed), "Run parser over name candidate string"
        if self.parsed["parsed"]:
            hc = NameExtractor(self.parsed, with_nlp)
            canonical = hc.canonical_list()
            if canonical:
                self.name_string.adjust(canonical, self.parsed["positions"])
                return True
            else: return False
        else: return False
