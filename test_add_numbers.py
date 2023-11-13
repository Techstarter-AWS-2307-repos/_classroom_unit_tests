import unittest
import os

from add_numbers import add_two_numbers


class Test(unittest.TestCase):
    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")

    def test_addition(self):
        self.assertEqual(add_two_numbers(1, 2), 3)
        self.assertEqual(add_two_numbers(-1, 1), 0)
        self.assertEqual(add_two_numbers(0, 0), 0)
