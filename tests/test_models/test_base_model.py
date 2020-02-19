#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class with test cases for the Base class"""

    def test_doc(self):
        """[BaseModel] Testing if doc exist"""
        self.assertTrue(len(BaseModel.__doc__) > 0)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 0)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 0)
        self.assertTrue(len(BaseModel.save.__doc__) > 0)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 0)

    def test_attrib(self):
        """[BaseModel] Testing attribute assignment"""
        b1 = BaseModel()
        b1.name = "Holberton"
        b1.my_number = 89
        self.assertAlmostEqual(b1.name, "Holberton")
        self.assertAlmostEqual(b1.my_number, 89)

    def test_to_dict(self):
        """[BaseModel] Testing to_dict method"""
        bm = BaseModel()
        baseDict = bm.to_dict()
        self.assertEqual(bm.__class__.__name__, 'BaseModel')
        self.assertIsInstance(baseDict['created_at'], str)
        self.assertIsInstance(baseDict['updated_at'], str)
        self.assertIsInstance(baseDict['id'], str)

    def test__str__(self):
        """[BaseModel] Testing __str__ method"""
        bm = BaseModel()
        bmStr = str(bm)
        strTest = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(bmStr, strTest)

    def test_save(self):
        """[BaseModel] Testing save method"""
        base = BaseModel()
        bm1 = base.to_dict()
        base.save()
        bm2 = base.to_dict()
        self.assertNotEqual(bm1["updated_at"], bm2["updated_at"])
