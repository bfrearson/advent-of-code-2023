import unittest
import day_2
from Game import Game, Set

test_data = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

test_games = [Game.from_string(line) for line in test_data.splitlines()]

class TestDay2(unittest.TestCase):
    def test_possible_game_numbers(self):
        self.assertEqual([1,2,5], day_2.possible_game_numbers(test_games))

    def test_game_sum(self):
        self.assertEqual(8, day_2.game_sum([1,2,5]))# add assertion here

    def test_minimum_Game_sets(self):
        self.assertEqual([Set(4,2,6), Set(1,3,4), Set(20,13,6), Set(14,3,15), Set(6,3,2)], [game.minimum_set() for game in test_games])
    def test_minimum_Game_power(self):
        self.assertEqual(48, test_games[0].minimum_power())
    def test_minimum_power(self):
        self.assertEqual(2286, day_2.minimum_power(test_games))

if __name__ == '__main__':
    unittest.main()
