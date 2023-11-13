import unittest
import os
import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(parent_dir))

from add_numbers import add_two_numbers


class TestAddTwoNumbers(unittest.TestCase):
    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(parent_dir.is_file(file_name), f"{file_name} does not exist")

    def test_addition(self):
        self.assertEqual(add_two_numbers(1, 2), 3)
        self.assertEqual(add_two_numbers(-1, 1), 0)
        self.assertEqual(add_two_numbers(0, 0), 0)
