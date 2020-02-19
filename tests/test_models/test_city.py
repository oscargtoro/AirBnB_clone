#!/usr/bin/python3
"""unittests for this project"""
import unittest
import os
from models.city import City


class TestCity(unittest.TestCase):
    """Class with test cases for the City class"""

    def test_cityperm(self):
        """[City] test file city.py permissions"""
        self.assertTrue(os.access('models/city.py', os.R_OK))
        self.assertTrue(os.access('models/city.py', os.W_OK))
        self.assertTrue(os.access('models/city.py', os.X_OK))

    def test_attrib(self):
        """Test attribute assignment"""
        b1 = City()
        b1.state_id = "1"
        b1.name = "Cali"
        self.assertAlmostEqual(b1.name, "Cali")
