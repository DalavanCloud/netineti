"""Tests for  ListData and all lists it supports"""

import unittest
from netineti.list_data import ListData

class TestListData(unittest.TestCase):
    """Test methods from blad, grey and white lists"""
    def setUp(self):
        self.listdata = ListData()

    def test_contains(self):
        """Check if we can lookup names in lists in reasonable amount of time"""
        for i in range(1, 100000): # pylint: disable=W0612
            self.assertTrue(self.listdata.black.contains("aaa"))
            self.assertFalse(self.listdata.black.contains("Pomatomus"))

            self.assertTrue(self.listdata.common.contains("common"))
            self.assertFalse(self.listdata.common.contains("Pomatomus"))

            self.assertTrue(self.listdata.species.contains("major"))
            self.assertFalse(self.listdata.species.contains("building"))

            self.assertTrue(self.listdata.genera.contains("Plantago"))
            self.assertFalse(self.listdata.genera.contains("building"))

            self.assertTrue(self.listdata.uninomials.contains("Aves"))
            self.assertFalse(self.listdata.uninomials.contains("Major"))

            self.assertTrue(self.listdata.grey_species.contains("academia"))
            self.assertTrue(self.listdata.grey_species.contains("major"))
            self.assertFalse(self.listdata.grey_species.contains("saltator"))

            self.assertTrue(self.listdata.grey_genera.contains("Cancer"))
            self.assertFalse(self.listdata.grey_genera.contains("Pomatomus"))

            self.assertTrue(
                self.listdata.grey_genera.contains_species("Cancer", "aeneus")
            )
            self.assertFalse(
                self.listdata.grey_genera
                .contains_species("Cancer", "treatment")
            )
