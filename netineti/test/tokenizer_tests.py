# -*- coding: utf-8 -*-
"""Test functions from helper module"""
import unittest
from netineti.tokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):
    """Test tokenizer functions"""

    def test_tokenize(self):
        """Takes text and splits it into tokens removing word splits in the end
        of a line"""
        text = """The text has words di-\nvided by a vari - \r\nety of
        word-splitting combinations of \n, \r and - .\n When \r
        and - are not together '\n' and '\r' work as normal space."""
        tokens = Tokenizer(text).tokenize()
        words = [w.verbatim for w in tokens]
        self.assertEqual(tokens[0].verbatim, 'The')
        self.assertEqual(text[tokens[0].start:tokens[0].end], 'The')
        self.assertEqual(tokens[4].verbatim, 'divided')
        self.assertEqual(text[tokens[4].start:tokens[4].end], 'di-\nvided')
        self.assertEqual(tokens[4].verbatim, 'divided')
        self.assertEqual(text[tokens[4].start:tokens[4].end], 'di-\nvided')
        self.assertEqual(tokens[6].verbatim, 'variety')
        self.assertEqual(text[tokens[6].start:tokens[6].end], 'vari - \r\nety')
        self.assertEqual(tokens[-1].verbatim, 'space.')
        self.assertEqual(text[tokens[-1].start:tokens[-1].end], 'space.')
        self.assertEqual(words, ['The', 'text', 'has', 'words', 'divided',
                                 'by', 'variety', 'of', 'word-splitting',
                                 'combinations', 'of', 'and', 'When', 'and',
                                 'are', 'not', 'together', 'and', 'work', 'as',
                                 'normal', 'space.'])

