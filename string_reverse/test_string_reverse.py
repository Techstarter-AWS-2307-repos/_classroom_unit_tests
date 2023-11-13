import unittest
import os
from string_reverse import string_reverse

class Test(unittest.TestCase):
    def test_file_exists(self):
        file_name = self.__module__.split('.')[-1] + '.py'
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")

    def test_string_reverse(self):
        self.assertEqual(string_reverse("hello"), "olleh")
        self.assertEqual(string_reverse("Python"), "nohtyP")