# test_mkdocsmaterial.py
"""
Tests for MkdocsMaterial module.
"""

import unittest
from mkdocsmaterial import MkdocsMaterial

class TestMkdocsMaterial(unittest.TestCase):
    """Test cases for MkdocsMaterial class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MkdocsMaterial()
        self.assertIsInstance(instance, MkdocsMaterial)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MkdocsMaterial()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
