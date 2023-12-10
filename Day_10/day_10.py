def solve_maze(maze_string):
    rows = maze_string.splitlines()
    row, col = find_start_position(rows)
    if row > 0 and rows[row - 1][col] in ["|", "J", "L"]:
        steps = follow_route(row - 1, col, row, col, rows)
        if steps is not None:
            return steps
    if row < len(rows) - 1 and rows[row + 1][col] in ["|", "F", "7"]:
        steps = follow_route(row + 1, col, row, col, rows)
        if steps is not None:
            return steps
    if col > 0 and rows[row][col - 1] in ["-", "F", "L"]:
        steps = follow_route(row, col - 1, row, col, rows)
        if steps is not None:
            return steps
    if col < len(rows[0]) - 1 and rows[row][col + 1] in ["-", "J", "7"]:
        steps = follow_route(row, col + 1, row, col, rows)
        if steps is not None:
            return steps
    return None

def find_start_position(rows):
    for row_index, row in enumerate(rows):
        for col_index, char in enumerate(row):
            if char == "S":
                return row_index, col_index


def follow_route(row, col, prev_row, prev_col, rows):
    current_node = rows[row][col]

    def get_new_position():
        if current_node == "|":
            return row + row - prev_row, col
        if current_node == "-":
            return row, col + col - prev_col
        if current_node == "L":
            next_row = row - 1 if row - prev_row == 0 else row
            next_col = col + 1 if col - prev_col == 0 else col
            return next_row, next_col
        if current_node == "J":
            next_row = row - 1 if row - prev_row == 0 else row
            next_col = col - 1 if col - prev_col == 0 else col
            return next_row, next_col
        if current_node == "7":
            next_row = row + 1 if row - prev_row == 0 else row
            next_col = col - 1 if col - prev_col == 0 else col
            return next_row, next_col
        if current_node == "F":
            next_row = row + 1 if row - prev_row == 0 else row
            next_col = col + 1 if col - prev_col == 0 else col
            return next_row, next_col

    steps = 1
    while current_node != "S":
        if current_node == ".":
            return None
        print(current_node)
        new_row, new_col = get_new_position()
        prev_row, prev_col = row, col
        row, col = new_row, new_col
        current_node = rows[row][col]
        steps += 1


    return steps/2


if __name__ == "__main__":
    maze = open("input.txt").read()
    print(f"Part 1: {solve_maze(maze)}")