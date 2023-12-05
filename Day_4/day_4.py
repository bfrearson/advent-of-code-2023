# Part 1
def get_card_score(card: str):
    match_count = get_card_match_count(card)
    return pow(2, match_count - 1) if match_count > 0 else 0


# Part 2
def get_card_match_count(card: str):
    numbers = card.split(":")[1].split("|")
    winning_numbers = numbers[0].strip().split(" ")
    numbers_to_match = numbers[1].split(" ")

    match_count = 0
    for number in numbers_to_match:
        if number.isnumeric() and number in winning_numbers:
            match_count += 1

    return match_count


def get_total_cards(cards: str):
    lines = cards.splitlines()

    # It would be faster to store the running total of each card, and use that to update the subsequent totals of the
    # cards it generates.
    for line in lines:
        current_card_number = int(line.split(":")[0].split(" ")[-1])
        match_count = get_card_match_count(line)
        if match_count > 0:
            lines.extend(
                [lines[card_index] for card_index in range(current_card_number, current_card_number + match_count)])
    return len(lines)


if __name__ == "__main__":
    with open("input.txt") as input:
        test_cards = input.read()
    print(f"part 1, game sum: {sum(get_card_score(card) for card in test_cards.splitlines())}")
    print(f"part 2, total cards: {get_total_cards(test_cards)}")
