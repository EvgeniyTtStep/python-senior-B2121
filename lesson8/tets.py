import unittest
from main import *


class MyTest(unittest.TestCase):

    def test_args(self):
        self.assertEqual(add(2, 3), 4)

    def test_args_negative(self):
        self.assertEqual(add(-2, -2), -4)


if __name__ == "__main__":
    unittest.main()
