import numpy as np


def get_time_bounds(time, distance):
    polynomial = np.polynomial.polynomial.Polynomial([distance, -time, 1])
    return polynomial.roots()


def find_integer_solutions(time, distance):
    roots = get_time_bounds(time, distance)
    int_range = range(int(roots[0]) + 1, int(np.ceil(roots[1])))
    return list(int_range)


def get_all_record_permutations(input):
    times, distances = input.splitlines()
    times = [int(time) for time in times.split(":")[1].split()]
    distances = [int(distance) for distance in distances.split(":")[1].split()]

    running_product_of_permutations = 1
    for index in range(len(times)):
        time = times[index]
        distance = distances[index]
        permutations = len(find_integer_solutions(time, distance))
        print(permutations)
        running_product_of_permutations *= permutations

    return running_product_of_permutations

def get_compressed_permutations(input):
    time, distance = input.splitlines()
    time = int(time.split(":")[1].replace(" ", ""))
    distance = int(distance.split(":")[1].replace(" ", ""))
    return len(find_integer_solutions(time, distance))


if __name__ == "__main__":
    input = open("input.txt", "r").read()
    print(f"part 1:{get_all_record_permutations(input)}")
    print(f"part 2:{get_compressed_permutations(input)}")
