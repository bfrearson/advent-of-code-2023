# Use recursion to find a common difference of 0. Walk back up, providing the next value

def compute_next_value(sequence: [int]) -> int:
    def find_differences(input: [int]):
        differences = []
        for index, value in enumerate(input[:-1]):
            differences.append(input[index + 1] - value)
        return differences

    differences = find_differences(sequence)

    if all(diff == 0 for diff in differences):
        return sequence[0]
    else:
        difference = compute_next_value(differences)
        return sequence[-1] + difference

if __name__ == "__main__":
    file = open("input.txt").read()
    sequences = [[int(number) for number in line.split()]for line in file.splitlines()]
    sum = 0
    for sequence in sequences:
        next_value = compute_next_value(sequence)
        sum += next_value
    print(sum)