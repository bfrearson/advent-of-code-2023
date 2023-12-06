import unittest
import textwrap
from day_5 import *

test_maps = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
class Day_5_tests(unittest.TestCase):
    # Part 1
    def test_map_value(self):
        map = textwrap.dedent("""\
        50 98 2
        52 50 48
        """)
        self.assertEqual(81, map_value(79, map))

    def test_map_seeds_to_location(self):
        locations = map_seeds_to_location(test_maps)
        self.assertEqual([82,43,86,35], locations)
        self.assertEqual(35, min(locations))

    # Part 2
    def test_map_seed_ranges_to_location(self):
        locations = map_seed_ranges_to_location(test_maps)
        self.assertEqual(46, min(locations))

if __name__ == '__main__':
    unittest.main()
