import unittest
from day_4 import *
test_cards = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
test_scores = [8,2,2,1,0,0]
class Day4Tests(unittest.TestCase):
    # Part 1
    def test_get_card_score(self):
        scores = []
        for line in test_cards.splitlines():
            scores.append(get_card_score(line))
        self.assertEqual(test_scores, scores)
        self.assertEqual(sum(scores), 13)
    # Part 2
    def test_get_total_cards(self):
        self.assertEqual(get_total_cards(test_cards), 30)


if __name__ == '__main__':
    unittest.main()
