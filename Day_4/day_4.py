def get_card_score(card: str):
    numbers = card.split(":")[1].split("|")
    winning_numbers = numbers[0].strip().split(" ")
    numbers_to_match = numbers[1].split(" ")

    match_count = 0
    for number in numbers_to_match:
        if number.isnumeric() and number in winning_numbers:
            print(f"{number} is in {winning_numbers}")
            match_count += 1

    return pow(2, match_count-1) if match_count > 0 else 0

if __name__ == "__main__":
    with open("input.txt") as input:
        test_cards = input.read()
    print(sum(get_card_score(card) for card in test_cards.splitlines()))