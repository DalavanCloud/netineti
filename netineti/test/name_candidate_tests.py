"""Tests for NameCandidate class"""
import unittest
from netineti.tokenizer import Tokenizer
from netineti.name_parser import NameParser
from netineti.name_candidate import NameCandidate

class TestNameCandidate(unittest.TestCase):
    """Test tokenizer functions"""
    @classmethod
    def setUpClass(cls):
        """ Sets parser once for all tests.
        Run `nosetests` -s to see print output """
        print("Starting parser")
        super(TestNameCandidate, cls).setUpClass()
        cls.parser = NameParser()
        cls.parser.start()

    @classmethod
    def tearDownClass(cls):
        """ Sets parser once for all tests.
        Run `nosetests` -s to see print output """
        print("Stopping parser")
        super(TestNameCandidate, cls).tearDownClass()
        cls.parser.stop()

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

    def test_select(self):
        """NameCandidate select returns true if there is a name, false if there
        is not"""
        text = "Homo sapiens is an ape"
        token, tokens = self.__class__.prepare_data(text)
        nc = NameCandidate(token, tokens)
        nc.parsed_raw = self.__class__.parser.parse(text)
        self.assertTrue(nc.select())
        self.assertEqual(nc.name_string, "Homo sapiens")
