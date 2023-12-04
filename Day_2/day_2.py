from Game import Game

max_red = 12
max_green = 13
max_blue = 14


def possible_game_numbers(games:[Game]):
    possible_game_numbers = []
    for game in games:
        is_valid = True
        game_num = game.game_num
        sets = game.sets
        for set in sets:
            red = set.red
            green = set.green
            blue = set.blue
            if red > max_red or green > max_green or blue > max_blue:
                is_valid = False
        if is_valid:
            possible_game_numbers.append(game_num)

    return possible_game_numbers

def game_sum(games: [int]):
    sum = 0
    for game in games:
        sum += game
    return sum

def minimum_power(games: [Game]):
    sum = 0
    for game in games:
        sum += game.minimum_power()
    return sum

if __name__ == '__main__':
    games = [Game.from_string(line) for line in open('input.txt').read().splitlines()]
    print("Game sum:", game_sum(possible_game_numbers(games)))
    print("Minimum power:", minimum_power(games))