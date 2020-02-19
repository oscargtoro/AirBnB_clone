#!/usr/bin/python3
"""unittests for this project"""
import unittest
import os
from models.place import Place


class TestPlace(unittest.TestCase):
    """Class with test cases for the Place class"""

    def test_attrib(self):
        """[Place] Test attribute assignment"""
        b1 = Place()
        self.assertAlmostEqual(b1.number_rooms, 0)

    def test_doc(self):
        """[Place] Testing if doc exist"""
        self.assertTrue(len(Place.__doc__) > 0)
        self.assertTrue(len(Place.__str__.__doc__) > 0)
        self.assertTrue(len(Place.to_dict.__doc__) > 0)
        self.assertTrue(len(Place.save.__doc__) > 0)
        self.assertTrue(len(Place.__init__.__doc__) > 0)

    def test_userperm(self):
        """[Place] test file palce.py permissions"""
        self.assertTrue(os.access('models/place.py', os.R_OK))
        self.assertTrue(os.access('models/place.py', os.W_OK))
        self.assertTrue(os.access('models/place.py', os.X_OK))

    def test_save(self):
        """[Place] Testing save method"""
        place = Place()
        place1 = place.to_dict()
        place.save()
        place2 = place.to_dict()
        self.assertNotEqual(place1["updated_at"], place2["updated_at"])
