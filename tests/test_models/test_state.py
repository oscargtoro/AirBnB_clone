#!/usr/bin/python3
"""unittests for this project"""
import unittest
import os
from models.state import State


class TestState(unittest.TestCase):
    """Class with test cases for the State class"""

    def test_stateperm(self):
        """[State] test file state.py permissions"""
        self.assertTrue(os.access('models/state.py', os.R_OK))
        self.assertTrue(os.access('models/state.py', os.W_OK))
        self.assertTrue(os.access('models/state.py', os.X_OK))

    def test_attrib(self):
        """[State] Test attribute assignment"""
        b1 = State()
        b1.name = "Lousiana"
        self.assertAlmostEqual(b1.name, "Lousiana")
