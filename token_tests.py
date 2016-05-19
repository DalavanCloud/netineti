# -*- coding: utf-8 -*-
"""Test functions from Token module"""
import unittest
from netineti.token import Token

class TestTokenizer(unittest.TestCase):
    """Test tokenizer functions"""

    def test_is_tokenizable(self):
        """Checks if a string is worth to tokenize"""
        #length more than one char
        self.assertFalse(Token.is_tokenizable('a'))
        self.assertTrue(Token.is_tokenizable('a!'))
        #should have at least one letter
        self.assertFalse(Token.is_tokenizable('#!$^^%,.'))
        self.assertTrue(Token.is_tokenizable('h?'))
        self.assertTrue(Token.is_tokenizable('?...mm'))

    def test_token(self):
        """Creates Token instance with default accessors"""
        token = Token(0, 4, 'hello!')
        self.assertEqual(token.start, 0)
        self.assertEqual(token.end, 4)
        self.assertEqual(token.verbatim, 'hello!')

