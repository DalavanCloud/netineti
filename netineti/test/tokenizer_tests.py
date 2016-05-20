# -*- coding: utf-8 -*-
"""Test functions from helper module"""
import unittest
from netineti.tokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):
    """Test tokenizer functions"""

    def test_tokenize_text(self):
        """Takes text and splits it into tokens removing word splits in the end
        of a line"""
        text = """The text has words di-\nvided by a vari - \r\nety of
        word-splitting combinations of \n, \r and - .\n When \r
        and - are not together '\n' and '\r' work as normal space."""
        tokens = Tokenizer(text).tokenize()
        words = [w.verbatim for w in tokens]
        self.assertEqual(tokens[-1].verbatim, 'The')
        self.assertEqual(text[tokens[-1].start:tokens[-1].end], 'The')
        self.assertEqual(tokens[-5].verbatim, 'divided')
        self.assertEqual(text[tokens[-5].start:tokens[-5].end], 'di-\nvided')
        self.assertEqual(tokens[-5].verbatim, 'divided')
        self.assertEqual(text[tokens[-5].start:tokens[-5].end], 'di-\nvided')
        self.assertEqual(tokens[-8].verbatim, 'variety')
        self.assertEqual(text[tokens[-8].start:tokens[-8].end],
                         'vari - \r\nety')
        self.assertEqual(tokens[0].verbatim, 'space.')
        self.assertEqual(text[tokens[0].start:tokens[0].end], 'space.')
        self.assertEqual(words, ['space.', 'normal', 'as', 'work', "'", "'",
                                 'and', "'", "'", 'together', 'not', 'are',
                                 '-', 'and', 'When', '.', '-', 'and', ',',
                                 'of', 'combinations', 'word-splitting',
                                 'of', 'variety', 'a', 'by', 'divided',
                                 'words', 'has', 'text', 'The'])

    def test_tokenize_unicode(self):
        """Takes text with non-latin chars and still calculates indices
        correctly"""
        text = """ Homo sapiens это челoвек с большой буквы. Lets see if
        this will fly..."""
        tokens = Tokenizer(text).tokenize()
        words = [w.verbatim for w in tokens]
        from_indices = [text[t.start:t.end] for t in tokens]
        self.assertEqual(words, ['fly...', 'will', 'this', 'if', 'see', 'Lets',
                                 'буквы.', 'большой', 'с', 'челoвек',
                                 'это', 'sapiens', 'Homo'])
        self.assertEqual(words, from_indices)


    def test_tokenize_empty(self):
        """Deals with empty string"""
        text = ''
        tokens = Tokenizer(text).tokenize()
        self.assertEqual(tokens, [])
