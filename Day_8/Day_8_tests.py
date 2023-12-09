import unittest
from day_8 import *

test_network1 = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""
test_network2 = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
test_network2 = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

class Day_8_tests(unittest.TestCase):
    def test_follow_instructions(self):
        self.assertEqual(2, follow_instructions(test_network1))
        self.assertEqual(6, follow_instructions(test_network2))

    def test_follow_ghost_instructions(self):
        self.assertEqual(6, follow_ghost_instructions(test_network3))


if __name__ == '__main__':
    unittest.main()
