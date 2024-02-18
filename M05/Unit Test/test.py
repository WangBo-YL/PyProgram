import unittest
from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 3), Fraction(2, 4)]
        result = sum(data)
        self.assertEqual(result, 1)

    def test_list_float(self):
        """
        Test that it can sum a list of floats
        """
        data = [1.5, 2.3, 3.7]
        result = sum(data)
        self.assertEqual(result, 7.5)

    def test_list_mixed(self):
        """
        Test that it can sum a list of mixed types
        """
        data = [1, 2.5, 3]
        result = sum(data)
        self.assertEqual(result, 6.5)

    def test_list_empty(self):
        """
        Test that it can sum an empty list
        """
        data = []
        result = sum(data)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()


"""
The test results means the list of fractions being returned is not correct.
Traceback means that the sum() function is not being called correctly.
AssertionError means that the result is not being summed correctly.
"""