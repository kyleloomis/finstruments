import unittest
from functools import reduce
from operator import mul

from finstruments.common.enum import Average


class AverageTest(unittest.TestCase):
    def test_arithmetic_average(self):
        values = [1, 2, 3, 4, 5]
        result = Average.ARITHMETIC.apply(values)
        expected = sum(values) / len(values)
        self.assertAlmostEqual(result, expected, places=6)

    def test_geometric_average(self):
        values = [1, 2, 3, 4, 5]
        result = Average.GEOMETRIC.apply(values)

        # Compute product without math.prod()
        product = reduce(mul, values, 1)
        expected = product ** (1 / len(values))

        self.assertAlmostEqual(result, expected, places=6)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            Average.ARITHMETIC.apply([])

        with self.assertRaises(ValueError):
            Average.GEOMETRIC.apply([])

    def test_unsupported_average(self):
        # Attempt to create a fake enum member for unsupported test
        with self.assertRaises(Exception):
            Average("UNSUPPORTED").apply([1, 2, 3])
