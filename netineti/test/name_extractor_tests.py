"""Tests for extracting name-strings from raw parsed data"""
import unittest
from netineti.name_parser import NameParser
from netineti.name_extractor import NameExtractor

class TestNameExtractor(unittest.TestCase):
    """Test config reader"""

    @classmethod
    def setUpClass(cls):
        """ Sets parser once for all tests.
        Run `nosetests` -s to see print output """
        print("Starting parser")
        super(TestNameExtractor, cls).setUpClass()
        cls.parser = NameParser()
        cls.parser.start()

    @classmethod
    def tearDownClass(cls):
        """ Sets parser once for all tests.
        Run `nosetests` -s to see print output """
        print("Stopping parser")
        super(TestNameExtractor, cls).tearDownClass()
        cls.parser.stop()

    def test_genus(self):
        """test extraction of a name-string from genus parsed data"""
        parsed = TestNameExtractor.parser.parse("Pomatomus")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), "Pomatomus")

    def test_genus_extended(self):
        """test extraction of a name-string from genus parsed data"""
        parsed = TestNameExtractor.parser.parse("Pomatomus is a genus")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), "Pomatomus")

    def test_name_string_from_species(self):
        """test extraction of a name-string from species parsed data"""
        parsed = TestNameExtractor.parser.parse("Pomatomus saltator")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), "Pomatomus saltator")

