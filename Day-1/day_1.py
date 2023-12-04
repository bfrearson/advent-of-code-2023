# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

import re

def calibrate_line(line: str) -> int:
    digits = []
    i = 0

    for char in line:
        if char.isdigit():
            digits.append(char)


    result = int(digits[0]+digits.pop())
    return result

def calibration_sum(input):
    return sum(calibrate_line(line) for line in input.splitlines())

if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read()
        result = calibration_sum(input)
        print(result)
