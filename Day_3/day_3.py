import re
symbols:[str] = ['-', '&', '@', '$', '*', '#', '/', '+', '=', '%']

def print_symbols():
    input = open('input.txt').read()
    symbols = set(())
    for char in input:
        if (char.isalnum() == False and char != ".") and char != "\n":
            symbols.add(char)
    print(symbols)

def get_symbols(string):
    symbol_positions = []
    lines = string.splitlines()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            for symbol in symbols:
                if lines[row][col] == symbol:
                    symbol_positions.append((col, row))
    return symbol_positions


def get_valid_numbers(schematic):
    valid_numbers = []
    lines = schematic.splitlines()

    for index in range(len(lines)):
        line = lines[index]
        pattern = r"(" + "\d+" + r")"
        regex = re.compile(pattern)
        matches = regex.finditer(line)

        def is_valid(match, lines):
            lower_column_index = max(match.regs[0][0] - 1, 0)
            upper_column_index = min(match.regs[0][1], match.endpos - 1)
            lower_row_index = max(index - 1, 0)
            upper_row_index = min(index + 1, len(lines) - 1)

            if match.group() == "367":
                print("match")

            for row in range(lower_row_index, upper_row_index + 1):
                for column in range(lower_column_index, upper_column_index + 1):
                    if re.search("[^a-zA-Z0-9.\n]", lines[row][column]):
                        return True

            debug_text = "\n".join(
                "".join(lines[row][col] for col in range(lower_column_index, upper_column_index))
                for row in range(lower_row_index, upper_row_index + 1)
            )
            print(" ")
            print(debug_text)
            print(" ")
            return False

        valid_numbers += [match.group() for match in matches if is_valid(match, lines)]

    return list(map(int, valid_numbers))

def sum_of_valid_numbers(schematic):
    valid_numbers = get_valid_numbers(schematic)
    print(valid_numbers)
    return sum(valid_numbers)

if __name__ == '__main__':
    input = open('input.txt').read()
    print("Engine sum", sum_of_valid_numbers(input))