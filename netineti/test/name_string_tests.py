"""Tests for extracting name-strings from raw parsed data"""
import unittest
from netineti.tokenizer import Tokenizer
from netineti.name_string import NameString

class TestNameString(unittest.TestCase):
    """Test Name String"""

    def test_init(self):
        """test extraction of a name-string from genus parsed data"""
        tokens = Tokenizer("""Pu-
        ma concolor crawls slow-
        ly, and then jumps farrrr. And this is not the end of the Story: Homo sapiens --
        is an ape. I think we told it is some other test
        already...""").tokenize()
        ns = NameString(tokens.pop(), tokens[-1:-15:-1])
        self.assertEqual(ns.name_string, "Puma concolor crawls slowly, and " +
                         "then jumps farrrr. And this is not the end of")
        self.assertEqual(ns.offsets[0:4],
                         [{0: {'offset': 0, 'position': 'start', 'token': 0}},
                          {4: {'offset': 14, 'position': 'end', 'token': 0}},
                          {5: {'offset': 15, 'position': 'start', 'token': 1}},
                          {13: {'offset': 23, 'position': 'end', 'token': 1}}])

