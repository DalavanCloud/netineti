"""Tests for  ListData and all lists it supports"""

import unittest
from netineti.list_data import ListData

class TestListData(unittest.TestCase):
    """Test methods from blad, grey and white lists"""
    def test_contains(self):
        """Check if we can lookup names in lists in reasonable amount of time"""
        for i in range(1, 10000): # pylint: disable=W0612
            l = ListData()
            self.assertTrue(l.in_black('aaa'))
            self.assertFalse(l.in_black('Pomatomus'))

            self.assertTrue(l.in_common("common"))
            self.assertFalse(l.in_common("Pomatomus"))

            self.assertFalse(l.in_species("major"))
            self.assertFalse(l.in_species("building"))

            self.assertTrue(l.in_genera("Plantago"))
            self.assertFalse(l.in_genera("building"))

            self.assertTrue(l.in_uninomials("Aves"))
            self.assertFalse(l.in_uninomials("Major"))

            self.assertTrue(l.in_grey_species("academia"))
            self.assertTrue(l.in_grey_species("major"))
            self.assertFalse(l.in_grey_species("saltator"))

            self.assertTrue(l.in_grey_genera("Cancer"))
            self.assertFalse(l.in_grey_genera("Pomatomus"))

            self.assertTrue(l.in_grey_genera_species("Cancer", "aeneus"))
            self.assertFalse(l.in_grey_genera_species("Cancer", "treatment"))
