from src.main import add

import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(add(3,4), 7)

