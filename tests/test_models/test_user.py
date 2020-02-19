#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class with test cases for the User class"""

    def test_password(self):
        """Test password assignment"""
        b1 = User()
        b1.password = "123456789"
        self.assertAlmostEqual(b1.password, "123456789")

    def test_email(self):
        """[User] Testing email assignment"""
        b1 = User()
        b1.email = "test@prueba.com"
        self.assertAlmostEqual(b1.email, "test@prueba.com")

    def test_first_name(self):
        """[User] Testing first_name assignment"""
        b1 = User()
        b1.first_name = "test"
        self.assertAlmostEqual(b1.first_name, "test")

    def test_last_name(self):
        """[User] Testing Last_name assignment"""
        b1 = User()
        b1.last_name = "test1"
        self.assertAlmostEqual(b1.last_name, "test1")
