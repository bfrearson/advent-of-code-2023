# Use recursion to find a common difference of 0. Walk back up, providing the next value

def compute_next_value(input: [int]):
    def find_differences(input: [int]):
        for index, value in enumerate(input[:-1]):
            differences = []
            differences.append(input[index + 1] - value)
            return differences
