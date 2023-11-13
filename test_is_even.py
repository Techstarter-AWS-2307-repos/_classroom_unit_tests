import unittest
import os
import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(parent_dir))

from is_even import is_even


class TestIsEven(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(os.path.dirname.isfile("is_even.py"), "is_even.py does not exist")

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(-1))
