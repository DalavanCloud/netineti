# -*- coding: utf-8 -*-
"""Test functions for features"""
import unittest
import netineti.features as features
from netineti.token import Token

class TestFeaturesFunctions(unittest.TestCase):
    """Test token features functions"""

    def test_is_capitalized(self):
        """Checks if a word is capitalized"""
        self.assertTrue(features.is_capitalized("Hello"))
        self.assertTrue(features.is_capitalized("Ælita"))
        self.assertFalse(features.is_capitalized("Ēary"))
        self.assertFalse(features.is_capitalized("hello"))
        self.assertFalse(features.is_capitalized("D"))

    def test_is_token(self):
        """Checks if we can distinguish Token from everything else"""
        t = Token(0, 2, "ya")
        nt = 23
        self.assertTrue(features.is_token(t))
        self.assertFalse(features.is_token(nt))

    def test_is_like_hybrid_sign(self):
        """Checks if words looks like a hybrid sign"""
        self.assertTrue(features.is_like_hybrid_sign("x"))
        self.assertTrue(features.is_like_hybrid_sign("X"))
        self.assertTrue(features.is_like_hybrid_sign("×"))
        self.assertTrue(features.is_like_hybrid_sign("×ADD"))
        self.assertTrue(features.is_like_hybrid_sign("xA."))
        self.assertFalse(features.is_like_hybrid_sign("XA."))
        self.assertFalse(features.is_like_hybrid_sign("bD"))
        self.assertFalse(features.is_like_hybrid_sign("c"))

    def test_is_known_uninomial(self):
        """Checks if a word is known uninomial word"""
        self.assertTrue(features.is_known_uninomial("Animalia"))
        self.assertFalse(features.is_known_uninomial("hello"))

    def test_is_known_genus(self):
        """Checks if a word is known genus word"""
        self.assertTrue(features.is_known_genus("Parus"))
        self.assertFalse(features.is_known_genus("Hello"))
        self.assertTrue(features.is_known_genus("Cancer"))

    def test_is_known_species(self):
        """Checks if a word is a known species epithet"""
        self.assertTrue(features.is_known_species("saltator"))
        self.assertFalse(features.is_known_species("computerized"))
        self.assertTrue(features.is_known_species("major"))
