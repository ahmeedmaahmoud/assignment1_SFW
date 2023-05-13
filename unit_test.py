import unittest
from math_operation import *

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(add(6,9), 15, "Should be 15")
    def test_sum2(self):
        self.assertEqual(add(9,9), 18, "Should be 18")
    def test_sum3(self):
        self.assertEqual(add(1,1), 2, "Should be 2")        


if __name__ == '__main__':
    unittest.main()
