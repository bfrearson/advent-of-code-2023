def follow_instructions(instructions):
    lines = instructions.splitlines()
    instruction = lines[0]
    nodes = [line.split(" = ") for line in lines[2:]]
    nodes = {node[0]: node[1][1:-1].split(", ") for node in nodes}
    current_key = "AAA"
    steps = 0
    while current_key != "ZZZ":
        for char in instruction:
            if char == "L":
                next_key = nodes[current_key][0]
            else:
                next_key = nodes[current_key][1]
            steps += 1
            if next_key == "ZZZ":
                return steps
            current_key = next_key

    return steps

if __name__ == "__main__":
    with open("input.txt") as f:
        instructions = f.read()
    print(follow_instructions(instructions))