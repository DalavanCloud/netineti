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
        self.assertEqual(
            [ns.offsets[k]['offset'] for k in sorted(ns.offsets.keys())],
            [0, 14, 15, 23, 24, 30, 31, 48, 49, 52, 53, 57, 58, 63, 64, 71,
            72, 75, 76, 80, 81, 83, 84, 87, 88, 91, 92, 95, 96, 98])
