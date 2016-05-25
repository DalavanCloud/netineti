"""Tests for NameCandidate class"""
import unittest
from netineti.tokenizer import Tokenizer
from netineti.name_candidate import NameCandidate

class TestNameCandidate(unittest.TestCase):
    """Test tokenizer functions"""

    @staticmethod
    def prepare_data(text):
        """Sets tokens list and a token from text"""
        tokens = Tokenizer(text).tokenize()
        token = tokens.pop()
        return [token, tokens]

    def test_constructor(self):
        """NameCandidate __init__ creates the class instance"""
        token, tokens = self.__class__.prepare_data("Homo sapiens is an ape")
        nc = NameCandidate(token, tokens)
        self.assertTrue(nc.is_promising())
