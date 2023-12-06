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


if __name__ == "__main__":
    input = open("input.txt", "r").read()
    print(get_all_record_permutations(input))
