#!/usr/bin/python3
"""unittests for this project"""
import unittest
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class with test cases for the Amenity class"""

    def test_amenityperm(self):
        """[Amenity] test file amenity.py permissions"""
        self.assertTrue(os.access('models/amenity.py', os.R_OK))
        self.assertTrue(os.access('models/amenity.py', os.W_OK))
        self.assertTrue(os.access('models/amenity.py', os.X_OK))

    def test_attrib(self):
        """Test attribute assignment"""
        b1 = Amenity()
        b1.name = "fireplace"
        self.assertAlmostEqual(b1.name, "fireplace")
