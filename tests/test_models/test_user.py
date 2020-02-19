#!/usr/bin/python3
"""unittests for this project"""
import unittest
import os
from models.user import User


class TestUser(unittest.TestCase):
    """Class with test cases for the User class"""

    def test_userperm(self):
        """[User] test file user.py permissions"""
        self.assertTrue(os.access('models/user.py', os.R_OK))
        self.assertTrue(os.access('models/user.py', os.W_OK))
        self.assertTrue(os.access('models/user.py', os.X_OK))

    def test_save(self):
        """Test validation updated_at"""
        b1 = User()
        up1 = b1.updated_at
        b1.save()
        up2 = b1.updated_at
        b1.save()
        self.assertNotEqual(up1, up2)

    def test_instance(self):
        """Test validation instance"""
        b1 = User()
        self.assertIsInstance(b1, User)

    def test_access(self):
        """Test access file"""
        access = os.access("models/user.py", os.R_OK)
        self.assertTrue(access, "Read permissions")

    def test_to_dict(self):
        """[BaseModel] Testing to_dict method"""
        user = User()
        userDict = user.to_dict()
        self.assertEqual(user.__class__.__name__, 'User')
        self.assertIsInstance(userDict['created_at'], str)
        self.assertIsInstance(userDict['updated_at'], str)
        self.assertIsInstance(userDict['id'], str)

    def test__str__(self):
        """[User] Testing __str__ method"""
        user = User()
        userStr = str(user)
        strTest = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(userStr, strTest)
