import unittest
import textwrap
from day_3 import *
test_engine ="""\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

test_engine2 ="""\
.......................*......*
...910*...............233..189.
2......391.....789*............
...................983.........
0........106-...............226
.%............../.............$
...*......$812.812..812..851...
.99.711..............0....*....
...........................113.
28*.....411....%..............."""
test_engine3 ="""\
...........
.52..52.52*
@..........
"""
class Day_3_tests(unittest.TestCase):
    def test_get_symbols(self):
        self.assertEqual([(3,1),(6,3),(3,4),(5,5),(3,8),(5,8)], get_symbols(test_engine))

    def test_get_valid_numbers(self):
        self.assertEqual([467, 35, 633, 617, 592, 755, 664, 598], get_valid_numbers(test_engine))
        self.assertEqual([111], get_valid_numbers("111+"))
        self.assertEqual([111], get_valid_numbers("-111"))
        self.assertEqual([111], get_valid_numbers(textwrap.dedent("""\
        ...*
        .111\
                                                  """)))
        self.assertEqual([111], get_valid_numbers(textwrap.dedent("""\
        ...*
        111.\
                                                  """)))
        self.assertEqual([], get_valid_numbers(textwrap.dedent("""\
            1111
            111.
        """)))

    def test_sum_of_valid_numbers(self):
        self.assertEqual(4361, sum_of_valid_numbers(test_engine))
        self.assertEqual(7253, sum_of_valid_numbers(test_engine2))
        self.assertEqual(104, sum_of_valid_numbers(test_engine3))


if __name__ == '__main__':
    unittest.main()
