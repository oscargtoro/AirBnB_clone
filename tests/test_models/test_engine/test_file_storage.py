#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Class with test cases for the Place class"""

    def test_doc(self):
        """[storage] Testing if doc exist"""
        self.assertTrue(len(storage.__doc__) > 0)
        self.assertTrue(len(storage.all.__doc__) > 0)
        self.assertTrue(len(storage.new.__doc__) > 0)
        self.assertTrue(len(storage.save.__doc__) > 0)
        self.assertTrue(len(storage.__init__.__doc__) > 0)
        self.assertTrue(len(storage.reload.__doc__) > 0)

    def test_all(self):
        """[storage] Testing all method output"""
        storageDict = storage.all()
        self.assertEqual(type(storageDict), dict)

    def test_new(self):
        """[storage] Testing new method"""
        bm = BaseModel()
        allbm = storage.all()
        objName = "{}.{}".format(type(bm).__name__, bm.id)
        self.assertIsNotNone(allbm[objName])
