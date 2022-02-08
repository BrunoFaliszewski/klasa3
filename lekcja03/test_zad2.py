import unittest
from zad2 import *

class TestCase(unittest.TestCase):

    def test_calculate(self):
        self.assertEqual(calculate_average([(2, 1), (4, 2), (5, 2)]), 4.0)
        
        with self.assertRaises(ValueError):
            calculate_average([(1, -1)])

if __name__ == "__main__":
    unittest.main()