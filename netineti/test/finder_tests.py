# -*- coding: utf-8 -*-
"""Test finder module"""
import unittest
from netineti.finder import NetiNeti
from netineti.trainer import NetiNetiTrainer

class TestFinder(unittest.TestCase):
    """Test helper functions"""

    @classmethod
    def setUpClass(TestFinder)
        self.nt = NetiNetiTrainer()

    def test_left_strip(self):
        """removes non-latin letters from the left of the token"""
        test_tokens = ['(hello', '#hello', 'H.!', 'шшhello', 'âhello']
        res = [helper.left_strip(token) for token in test_tokens]
        self.assertEqual(res, [('hello', 1), ('hello', 1),
                               ('H.!', 0), ('hello', 4), ('hello', 2)])

