"""Keeps and evaluates data that might contain scientific name"""
import netineti.features as features

class NameCandidate(object):
    """Keeps and pre-evaluates data that might contain scientific name"""

    def __init__(self, token, tokens):
        self.token = token
        self.offset = token.start
        self.tokens = tokens[0:15]
        self.string = None
        self.parsed_raw = None

    def is_promising(self):
        """Evaluates quality of NameCandidate"""
        w = self.token.verbatim
        is_a_maybe = len(self.token.verbatim) > 0 and features.is_capitalized(w)
        if not is_a_maybe:
            is_a_maybe = features.is_like_hybrid_sign(w)
        if is_a_maybe:
            self.string = (
                w + " " + " ".join([w.verbatim for w in reversed(self.tokens)])
            )
        return is_a_maybe
