#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models import storage


class TestFileStorage(unittest.TestCase):
    """Class with test cases for the Place class"""

    def test_doc(self):
        """Testing if doc exist """
        self.assertTrue(len(storage.__doc__) > 0)
        self.assertTrue(len(storage.all.__doc__) > 0)
        self.assertTrue(len(storage.new.__doc__) > 0)
        self.assertTrue(len(storage.save.__doc__) > 0)
        self.assertTrue(len(storage.__init__.__doc__) > 0)
        self.assertTrue(len(storage.reload.__doc__) > 0)
