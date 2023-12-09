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

def follow_ghost_instructions(instructions):
    lines = instructions.splitlines()
    instruction = lines[0]
    nodes = [line.split(" = ") for line in lines[2:]]
    nodes = {node[0]: node[1][1:-1].split(", ") for node in nodes}
    current_keys = []
    for key in nodes.keys()
        if key[2] == "A":
            current_keys.append(key)
    steps = 0
    at_end = False
    while at_end == False:
        for char in instruction:
            # Logic not finished here
            for index, current_key in enumerate(current_keys):
                if char == "L":
                    next_key = nodes[current_key][0]
                else:
                    next_key = nodes[current_key][1]
                current_keys[index] = next_key
            steps += 1
            if next_key == "ZZZ":
                return steps

    return steps

if __name__ == "__main__":
    with open("input.txt") as f:
        instructions = f.read()
    print(follow_instructions(instructions))