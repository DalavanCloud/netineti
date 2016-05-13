# -*- coding: utf-8 -*-
"""Test functions from helper module"""
import unittest
import netineti.helper as helper

class TestHelperFunctions(unittest.TestCase):
    """Test helper functions"""

    def test_left_strip(self):
        """removes non-latin letters from the left of the token"""
        test_tokens = ['(hello', '#hello', 'H.!', 'шшhello', 'âhello']
        res = [helper.left_strip(token) for token in test_tokens]
        self.assertEqual(res, [('hello', 1), ('hello', 1),
                               ('H.!', 0), ('hello', 4), ('hello', 2)])

    def test_right_strip(self):
        """removes non-latin letters from the right of the token"""
        test_tokens = ['hello)', 'hello,', 'H.', 'helloдада', 'helloâ']
        res = [helper.right_strip(token) for token in test_tokens]
        self.assertEqual(res, [('hello', -1), ('hello', -1), ('H', -1),
                               ('hello', -8), ('hello', -2)])

    def test_strip_token(self):
        """removes non-lating characters from both left and right"""
        test_tokens = ['(hello)', '#hello,', '1H.!', '123helloдада', 'âhelloâ']
        res = [helper.strip_token(token) for token in test_tokens]
        self.assertEqual(res, ['hello', 'hello', 'H', 'hello', 'hello'])

    def test_get_ascii_ratio(self):
        """calculates ratio between ascii7 letters and words"""
        tokens = ['однажды', '12345', 'wait', 'for', 'me!']
        res = helper.get_ascii_ratio(tokens)
        self.assertAlmostEqual(res, 0.4827586206896552)

    def test_get_words_slice(self):
        """cuts a slice out of a word from word list"""
        tokens = ['Once', 'upon', 'a', 'time', 'in', 'the', 'West']
        res = helper.get_words_slice(tokens, 1, 2, 4)
        self.assertEqual(res, 'on')
        res = helper.get_words_slice(tokens, 1, 5, 8)
        self.assertEqual(res, 'Null')
        res = helper.get_words_slice(tokens, 1, 3, None)
        self.assertEqual(res, 'n')

    def test_clean_token(self):
        """cleans tokens for classifier"""
        tokens = ["A.", "alba,", "#pubescens!"]
        res = helper.clean_token(tokens[0], tokens[1], tokens[2])
        self.assertEqual(res, ['A.', 'alba', 'pubescens'])

    def test_create_index(self):
        """returns index of a token and its offset from the start of a text"""
        test_tokens = ["hello", "bacon", "chocolate", "banana"]
        index = helper.create_index(test_tokens)
        self.assertEqual(index, {0:0, 1:6, 2:12, 3:22})

    def test_remove_trailing_period(self):
        """removes period if a token has more then one alphanumeric char"""
        tokens = ["A.", "a.", "abc.", "one,"]
        res = [helper.remove_trailing_period(t) for t in tokens]
        self.assertEqual(res, ['A.', 'a.', 'abc', 'one,'])


