# -*- coding: utf-8 -*-
"""Test functions from Token module"""
import unittest
from netineti.token import Token

class TestTokenizer(unittest.TestCase):
    """Test tokenizer functions"""

    def test_token(self):
        """Creates Token instance with default accessors"""
        token = Token(0, 4, 'hello!')
        self.assertEqual(token.start, 0)
        self.assertEqual(token.end, 4)
        self.assertEqual(token.verbatim, 'hello!')

