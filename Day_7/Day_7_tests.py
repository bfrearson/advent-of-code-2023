import unittest
from Hand import *
from day_7 import *

test_hands = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
class MyTestCase(unittest.TestCase):
    def test_hand_type(self):
        five_hand = Hand("AAAAA", 123)
        four_hand = Hand("AAAAK", 123)
        full_house_hand = Hand("AAAKK", 123)
        three_hand = Hand("AAAKQ", 123)
        two_pair_hand = Hand("AAKKJ", 123)
        pair_hand = Hand("AAKQJ", 123)
        high_card_hand = Hand("AKQJT", 123)
        self.assertEqual(HandType.FIVE_OF_A_KIND, five_hand.hand_type())
        self.assertEqual(HandType.FOUR_OF_A_KIND, four_hand.hand_type())
        self.assertEqual(HandType.FULL_HOUSE, full_house_hand.hand_type())
        self.assertEqual(HandType.THREE_OF_A_KIND, three_hand.hand_type())
        self.assertEqual(HandType.TWO_PAIR, two_pair_hand.hand_type())
        self.assertEqual(HandType.PAIR, pair_hand.hand_type())
        self.assertEqual(HandType.HIGH_CARD, high_card_hand.hand_type())

    def test_sort_hands(self):
        sorted_hands = sort_hands(test_hands)
        sorted_cards = [hand.cards for hand in sorted_hands]
        self.assertEqual(["32T3K", "KTJJT", "KK677", "T55J5", "QQQJA"], sorted_cards)

    def test_calculate_winnings(self):
        self.assertEqual(6440, calculate_winnings(test_hands))

if __name__ == '__main__':
    unittest.main()
