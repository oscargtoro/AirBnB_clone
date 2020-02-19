#!/usr/bin/python3
"""unittests for this project"""
import unittest
import os
from models.review import Review


class TestUser(unittest.TestCase):
    """Class with test cases for the Review class"""

    def test_doc(self):
        """[Review] Testing if doc exist"""
        self.assertTrue(len(Review.__doc__) > 0)
        self.assertTrue(len(Review.__str__.__doc__) > 0)
        self.assertTrue(len(Review.to_dict.__doc__) > 0)
        self.assertTrue(len(Review.save.__doc__) > 0)
        self.assertTrue(len(Review.__init__.__doc__) > 0)

    def test_reviewperm(self):
        """[Review] test file review.py permissions"""
        self.assertTrue(os.access('models/review.py', os.R_OK))
        self.assertTrue(os.access('models/review.py', os.W_OK))
        self.assertTrue(os.access('models/review.py', os.X_OK))

    def test_attrib(self):
        """Test attribute assignment"""
        b1 = Review()
        b1.place_id = "1"
        b1.user_id = "1"
        b1.text = "hello"
        self.assertAlmostEqual(b1.place_id, "1")
        self.assertAlmostEqual(b1.user_id, "1")
        self.assertAlmostEqual(b1.text, "hello")
