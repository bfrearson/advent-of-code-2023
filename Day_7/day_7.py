from Hand import Hand

def sort_hands(hands):
    custom_sort_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    custom_sort_order.reverse()

    def sort_key(hand):
        return (hand.hand_type().value, [custom_sort_order.index(card) for card in hand.cards])

    hands = [Hand(hand.split()[0], hand.split()[1]) for hand in hands.splitlines()]
    return sorted(hands, key=sort_key)

def calculate_winnings(input):
    hands = sort_hands(input)
    winnings = 0
    for index, hand in enumerate(hands):
        winnings += (index + 1) * int(hand.bid)
    return winnings

if __name__=="__main__":
    input = open("input.txt").read()
    print(f"Part 1: {calculate_winnings(input)}")