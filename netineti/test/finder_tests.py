# -*- coding: utf-8 -*-
"""Test finder module"""
import os
import pickle
import unittest
from netineti.finder import NetiNeti
from netineti.trainer import NetiNetiTrainer

USE_DUMP = True #set to True if you are not fixing algorithms (saves time)

PATH = os.path.dirname(os.path.realpath(__file__))
TRAINER_DUMP = PATH + '/../data/netineti_trainer_dump'

class TestFinder(unittest.TestCase):
    """Test helper functions"""

    @classmethod
    def setUpClass(cls):
        """ Sets trainer once per all tests.

        Run `nosetests` -s to see print output """
        print "Running trainer"
        super(TestFinder, cls).setUpClass()
        if USE_DUMP:
            cls.nt = pickle.load(open(TRAINER_DUMP, 'rb'))
        else:
            cls.nt = NetiNetiTrainer()
        cls.nn = NetiNeti(TestFinder.nt)

    def test_uninomial(self):
        """ Returns one found name from a text """
        res = TestFinder.nn.find_names("Poaceae are not spiders!")
        self.assertEqual(res, ('Poaceae', ['Poaceae'], [(0, 7)]))

    def test_binomial_exact_match(self):
        """ Returns one found name from a text containing only the name """
        res = TestFinder.nn.find_names("Pardosa moesta ")
        self.assertEqual(res, ('Pardosa moesta', ['Pardosa moesta'],
                               [(0, 14)]))

    def test_no_names(self):
        """ Returns empty result when no names found """
        res = TestFinder.nn.find_names("Nothing that looks like a name")
        self.assertEqual(res, ("", [], []))

    def test_black_dict(self):
        """ Discards names from black list """

    def test_multiple_names(self):
        """ Returns multiple names """
        res = TestFinder.nn.find_names("""
        Homo sapiens ate Pardosa moesta for breakfast, then
        Parus major ate Homo sapiens for lunch """)
        self.assertEqual(res, ('Homo sapiens\nPardosa moesta\nParus major',
                               ['Homo sapiens', 'Pardosa moesta',
                                'Parus major', 'Homo sapiens'],
                               [(9, 21), (26, 40), (69, 80), (85, 97)]))

    def test_commas_between_words(self):
        """ Commas after 1st or 2nd word means stop looking... """
        res = TestFinder.nn.find_names("""
        Homo, sapiens, sapiens are not subspecies name, because there
        are commas between them """)
        self.assertEqual(res, ('Homo sapiens sapiens',
                               ['Homo, sapiens, sapiens'], [(9, 31)]))
