class Set:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __eq__(self, other):
        if isinstance(other, Set):
            return (self.red == other.red) and (self.green == other.green) and (self.blue == other.blue)
        return False
class Game:
    def __init__(self, game_num, sets: [Set]):
        self.game_num = game_num
        self.sets = sets

    @classmethod
    def from_string(cls, game_string):
        game_num, sets_string = game_string.split(":")
        game_num = int(game_num.strip().split(" ")[-1])
        sets = []
        for set_string in sets_string.split(";"):
            set_string = set_string.strip()
            colors = set_string.split(", ")
            set = Set(0, 0, 0)
            for color in colors:
                count, color_name = color.split(" ")
                if color_name == "red":
                    set.red = int(count)
                if color_name == "green":
                    set.green = int(count)
                if color_name == "blue":
                    set.blue = int(count)
            sets.append(set)
        return cls(game_num, sets)

    def minimum_set(self):
        reds = [set.red for set in self.sets]
        greens = [set.green for set in self.sets]
        blues = [set.blue for set in self.sets]

        return Set(max(reds), max(greens), max(blues))

    def minimum_power(self):
        minimum_set = self.minimum_set()
        return minimum_set.red * minimum_set.green * minimum_set.blue
