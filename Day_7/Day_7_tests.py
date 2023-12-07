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


# Part 2
    def test_playing_jokers(self):
        five_hand = Hand("JJJJJ", 123)
        five_hand_with_j = Hand("AAAAJ", 123)
        five_hand_with_2j = Hand("AAAJJ", 123)
        five_hand_with_4j = Hand("AJJJJ", 123)

        four_hand_with_j = Hand("AAAKJ", 123)
        four_hand_with_2j = Hand("AAJKJ", 123)
        four_hand_with_3j = Hand("AJJKJ", 123)

        full_house_hand_with_J = Hand("AAKKJ", 123)

        three_hand_with_j = Hand("AAKQJ", 123)
        three_hand_with_2j = Hand("AKQJJ", 123)

        pair_hand_with_j = Hand("AKQTJ", 123)

        self.assertEqual(HandType.FIVE_OF_A_KIND, five_hand.hand_type(playing_jokers=True))
        self.assertEqual(HandType.FIVE_OF_A_KIND, five_hand_with_j.hand_type(playing_jokers=True))
        self.assertEqual(HandType.FIVE_OF_A_KIND, five_hand_with_2j.hand_type(playing_jokers=True))
        self.assertEqual(HandType.FIVE_OF_A_KIND, five_hand_with_4j.hand_type(playing_jokers=True))

        self.assertEqual(HandType.FOUR_OF_A_KIND, four_hand_with_j.hand_type(playing_jokers=True))
        self.assertEqual(HandType.FOUR_OF_A_KIND, four_hand_with_2j.hand_type(playing_jokers=True))
        self.assertEqual(HandType.FOUR_OF_A_KIND, four_hand_with_3j.hand_type(playing_jokers=True))

        self.assertEqual(HandType.FULL_HOUSE, full_house_hand_with_J.hand_type(playing_jokers=True))

        self.assertEqual(HandType.THREE_OF_A_KIND, three_hand_with_j.hand_type(playing_jokers=True))
        self.assertEqual(HandType.THREE_OF_A_KIND, three_hand_with_2j.hand_type(playing_jokers=True))

        self.assertEqual(HandType.PAIR, pair_hand_with_j.hand_type(playing_jokers=True))

    def test_calculate_winnings_with_jokers(self):
        self.assertEqual(5905, calculate_winnings(test_hands, playing_jokers=True))

if __name__ == '__main__':
    unittest.main()
