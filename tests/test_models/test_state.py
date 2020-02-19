#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Class with test cases for the State class"""

    def test_attrib(self):
        """Test attribute assignment"""
        b1 = State()
        b1.name = "Lousiana"        
        self.assertAlmostEqual(b1.name, "Lousiana")
