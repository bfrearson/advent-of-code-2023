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

class Day_8_tests(unittest.TestCase):
    def test_follow_instructions(self):
        self.assertEqual(2, follow_instructions(test_network1))
        self.assertEqual(6, follow_instructions(test_network2))



if __name__ == '__main__':
    unittest.main()
