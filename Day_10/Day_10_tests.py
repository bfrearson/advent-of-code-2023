import unittest
from day_10 import *
test_maze = """\
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""

class Day_10_tests(unittest.TestCase):
    def test_solve_maze(self):
        self.assertEqual(solve_maze(test_maze), 8)


if __name__ == '__main__':
    unittest.main()
