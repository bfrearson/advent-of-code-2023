# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

import regex as re

def calibrate_line(line: str) -> int:
    digits = []

    digits = findDigits(line)

    result = int(digits[0]+digits.pop())
    print(line, result)
    return result

def calibration_sum(input):
    return sum(calibrate_line(line) for line in input.splitlines())


def convert_to_digits(line):
    digit_mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }

    pattern = r"(" + "|".join(digit_mapping.keys()) + r")"
    regex = re.compile(pattern)

    match = regex.search(line)
    if match:
        digit_str = match.group(0)
        digit = digit_mapping[digit_str]
        line = line.replace(digit_str, digit, 1)
        line = convert_to_digits(line)
    return line

def findDigits(line:str) ->[int]:
    digit_mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }
    pattern = '(' + '|'.join(digit_mapping.keys()) + '|\\d' + ')'

    regex = re.compile(pattern)

    matches = regex.findall(line, overlapped=True)
    for index in range(len(matches)):
        matches[index] = convert_to_digits(matches[index])

    return matches

if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read()
        result = calibration_sum(input)
        print(result)
