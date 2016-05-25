"""Tests for parsing scientific names"""
import unittest
from netineti.name_parser import NameParser

class TestNameParser(unittest.TestCase):
    """Test NameParser"""

    def setUp(self):
        """Creates a parser and connection to it"""
        self.parser = NameParser()
        self.parser.start()

    def tearDown(self):
        """Stops parser"""
        self.parser.stop()

    def test_parse(self):
        """test that parsing works data"""
        res = self.parser.parse('Pomatomus saltatrix (Linnaeus, 1766)')
        self.assertTrue(res['parsed'])

    def test_no_parse(self):
        """test parser with a bad name"""
        res = self.parser.parse("this is not a name")
        self.assertFalse(res['parsed'])

    def test_no_parse_pos(self):
        """test parser with a bad name"""
        res = self.parser.pos("this is not a name")
        self.assertEqual(res, [])

    def test_parse_pos(self):
        """test parser with a good name"""
        res = self.parser.pos("Pomatomus saltatrix")
        self.assertEqual(res, [[u'genus', 0, 9],
                               [u'specific_epithet', 10, 19]])
