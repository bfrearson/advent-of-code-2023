import unittest
from day_9 import *
test_input = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
class Day_9_tests(unittest.TestCase):
    def test_compute_next_value(self):
        expected_values = [18, 28, 68]
        computed_values = []
        for line in test_input.splitlines():
            next_value = compute_next_value([int(number) for number in line.split()])
            computed_values.append(next_value)
        self.assertEqual(expected_values, computed_values)
        self.assertEqual(sum(expected_values), sum(computed_values))

    def test_compute_previous_value(self):
        expected_values = [-3, 0, 5]
        computed_values = []
        for line in test_input.splitlines():
            next_value = compute_previous_value([int(number) for number in line.split()])
            computed_values.append(next_value)
        self.assertEqual(expected_values, computed_values)
        self.assertEqual(sum(expected_values), sum(computed_values))

if __name__ == '__main__':
    unittest.main()
