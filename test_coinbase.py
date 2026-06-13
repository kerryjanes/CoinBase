# test_coinbase.py
"""
Tests for CoinBase module.
"""

import unittest
from coinbase import CoinBase

class TestCoinBase(unittest.TestCase):
    """Test cases for CoinBase class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinBase()
        self.assertIsInstance(instance, CoinBase)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinBase()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
