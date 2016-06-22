"""Tests for finding scientific names"""
import os
import pickle
import unittest
from netineti.name_finder import NameFinder
from netineti.trainer import NetiNetiTrainer

USE_DUMP = True #set to True if you are not fixing algorithms (saves time)

PATH = os.path.dirname(os.path.realpath(__file__))
TRAINER_DUMP = PATH + '/../data/netineti_trainer_dump'

class TestNameFinder(unittest.TestCase):
    """Test NameFinder"""

    @classmethod
    def setUpClass(cls):
        """ Sets trainer once per all tests.

        Run `nosetests` -s to see print output """
        print("Running trainer")
        super(TestNameFinder, cls).setUpClass()
        if USE_DUMP:
            cls.nt = pickle.load(open(TRAINER_DUMP, 'rb'))
        else:
            cls.nt = NetiNetiTrainer()
        cls.nf = NameFinder(TestNameFinder.nt)

    def test_find(self):
        """Test finding names"""
        text = """
        I have no Idea if this Document Contains names! Especially
        something like Homo sapiens Linneaus 1758, or may be Pardosa mo-
        esta..."""
        res = TestNameFinder.nf.find(text)
        self.assertTrue(res != 1)
