#!/usr/bin/python3
"""unittests for this project"""
import unittest
import os
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

    def test_save(self):
        """[storage] Testing save method"""
        try:
            os.remove(pt)
        except BaseException:
            pass
        base = BaseModel()
        storage.save()
        self.assertTrue(os.access('file.json', os.R_OK))
        try:
            os.remove(pt)
        except BaseException:
            pass

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
        try:
            os.remove(pt)
        except BaseException:
            pass

    def test_reload(self):
        """[storage] Testing reload method"""
        base = BaseModel()
        obj1 = storage.all()
        storage.save()
        storage.reload()
        obj2 = storage.all()
        self.assertEqual(obj1, obj2)
        try:
            os.remove(pt)
        except BaseException:
            pass
