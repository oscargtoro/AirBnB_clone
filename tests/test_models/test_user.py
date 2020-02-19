#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class with test cases for the User class"""

    def test_attrib(self):
        """Test attribute assignment"""
        b1 = User()
        b1.password = "123456789"        
        self.assertAlmostEqual(b1.password, "123456789")
