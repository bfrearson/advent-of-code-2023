import unittest
from day_6 import *

test_data = """\
Time:      7  15   30
Distance:  9  40  200
"""

class Day_6_tests(unittest.TestCase):
    def test_get_time_bounds(self):
        roots = get_time_bounds(7, 12)
        self.assertEqual(roots.tolist(), [3, 4])


    def test_find_integer_solutions(self):
        solutions = find_integer_solutions(7, 9)
        self.assertEqual(solutions, [2, 3, 4, 5])
        self.assertEqual(len(find_integer_solutions(15, 40)), 8)
        self.assertEqual(len(find_integer_solutions(30, 200)), 9)


    def test_get_all_record_permutations(self):
        permutations = get_all_record_permutations(test_data)
        self.assertEqual(permutations, 288)

if __name__ == '__main__':
    unittest.main()
