from enum import Enum
class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    def hand_type(self):
        counts = {}
        for card in self.cards:
            if counts.get(card):
                counts[card] += 1
            else:
                counts[card] = 1
        keys = list(counts)

        if counts[keys[0]] == 5:
            return HandType.FIVE_OF_A_KIND
        elif len(counts) == 2 and (counts[keys[0]] == 4 or counts[keys[1]] == 4):
            return HandType.FOUR_OF_A_KIND
        elif len(counts) == 2:
            return HandType.FULL_HOUSE
        elif len(counts) == 3 and (counts[keys[0]] == 3 or counts[keys[1]] == 3 or counts[keys[2]] == 3):
            return HandType.THREE_OF_A_KIND
        elif len(counts) == 3:
            return HandType.TWO_PAIR
        elif len(counts) == 4:
            return HandType.PAIR
        else:
            return HandType.HIGH_CARD
class HandType(Enum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    PAIR = 1
    HIGH_CARD = 0