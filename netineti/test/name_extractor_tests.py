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

    def test_genus_punctuation(self):
        """test extraction of a name-string from genus parsed data"""
        parsed = TestNameExtractor.parser.parse("Pomatomus. Sounds nice")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), "Pomatomus")
        parsed = TestNameExtractor.parser.parse("Pomatomus; saltator nice")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), "Pomatomus")
        parsed = TestNameExtractor.parser.parse("Pomatomus, saltator, alba")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), "Pomatomus")

    def test_name_string_from_species(self):
        """test extraction of a name-string from species parsed data"""
        parsed = TestNameExtractor.parser.parse("Pomatomus saltator")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), "Pomatomus saltator")
        parsed = TestNameExtractor.parser.parse("Pomatomus alba")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), "Pomatomus alba")
        parsed = TestNameExtractor.parser.parse("Homo sapiens is an ape")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), "Homo sapiens")

    def test_multiple_species(self):
        """test extraction of a name-string from species parsed data"""
        parsed = TestNameExtractor.parser.parse("Pomatomus saltator major alba")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), "Pomatomus saltator major alba")
        parsed = TestNameExtractor.parser.parse("""
        Pomatomus saltator major is found only in the dark corners""")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), "Pomatomus saltator major")
        parsed = TestNameExtractor.parser.parse("""Carex scirpoidea subsp.
        convoluta (Kükenthal 1909) D. A. Dunlop 1998 is quite
        long species name!""")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), "Carex scirpoidea convoluta")

    def test_punctuation_species(self):
        """test extraction of a name-string from species parsed data"""
        parsed = TestNameExtractor.parser.parse("Pomatomus saltator, major")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), "Pomatomus saltator")

    def test_named_hybrid(self):
        """test extraction of a name-string from hybrid parsed data"""
        parsed = TestNameExtractor.parser.parse("x Plantago major")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), '× Plantago major')

    def test_short_hybrid(self):
        """test extraction of a name-string from hybrid parsed data"""
        parsed = TestNameExtractor.parser.parse("Plantago x major")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), 'Plantago × major')

    def test_hybrid_formula(self):
        """test extraction of a name-string from hybrid parsed data"""
        parsed = TestNameExtractor.parser.parse("Plantago major x Parus major")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), 'Plantago major × Parus major')
        parsed = TestNameExtractor.parser.parse("Plantago major x saltator")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), 'Plantago major × saltator')
        parsed = TestNameExtractor.parser.parse("Plantago major x minor")
        ne = NameExtractor(parsed)
        self.assertEqual(ne.name_string(), 'Plantago major × minor')
