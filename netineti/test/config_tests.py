"""Tests reading data from configuration file"""
import unittest
from netineti.config import Config

class TestConfig(unittest.TestCase):
    """Test config reader"""

    def test_read(self):
        """test configuration data"""
        cnf = Config()
        self.assertEqual(cnf.config['gnparser']['host'], 'gnparser')
