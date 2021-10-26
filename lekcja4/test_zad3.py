import unittest

from zad3 import Rectangle


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.rectangle = Rectangle()

    def test_calculate_space(self):
        self.assertEqual(self.rectangle.calculate_space(((2, 2), (-2, -2))), 16.0)  # add assertion here

    def test_calculate_circuit(self):
        self.assertEqual(self.rectangle.calculate_circuit(((2, 2), (-2, -2))), 16.0)


if __name__ == '__main__':
    unittest.main()
