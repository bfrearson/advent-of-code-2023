import numpy as np

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

# Appears to be working, but takes a long time to run.
# Better to run the follow_instructions() function on each starting node and find the LCM of all nodes.
def follow_ghost_instructions(instructions):
    lines = instructions.splitlines()
    instruction = lines[0]
    nodes = [line.split(" = ") for line in lines[2:]]
    nodes = {node[0]: node[1][1:-1].split(", ") for node in nodes}
    current_keys = []
    for key in nodes.keys():
        if key[2] == "A":
            current_keys.append(key)
    steps = []
    at_end = False

    for start_key in current_keys:
        current_key = start_key
        at_end = False
        current_node_steps = 0
        while at_end != True:
            next_key = current_key
            for char in instruction:
                if char == "L":
                    next_key = nodes[current_key][0]
                else:
                    next_key = nodes[current_key][1]
                current_node_steps += 1
                if next_key[2] == "Z":
                    at_end = True
                    break
                current_key = next_key
        steps.append(current_node_steps)

    return np.lcm.reduce(steps)

def find_end_keys(instructions):
    lines = instructions.splitlines()
    instruction = lines[0]
    nodes = [line.split(" = ") for line in lines[2:]]
    nodes = {node[0]: node[1][1:-1].split(", ") for node in nodes}
    current_keys = []
    for key in nodes.keys():
        if key[2] == "A":
            current_keys.append(key)

    for start_key in current_keys:
        end_keys = []
        keys_are_complete = False
        while not keys_are_complete:
            current_key = start_key
            at_end = False
            while not at_end:
                next_key = current_key
                for char in instruction:
                    if char == "L":
                        next_key = nodes[current_key][0]
                    else:
                        next_key = nodes[current_key][1]
                    if next_key[2] == "Z":
                        at_end = True
                        break
                    current_key = next_key
            end_keys.append(next_key)
        print(f"start key:{start_key}, end keys: {end_keys}")

if __name__ == "__main__":
    with open("input.txt") as f:
        instructions = f.read()
    print(f"Part 1: {follow_instructions(instructions)}")
    print(f"Part 2: {follow_ghost_instructions(instructions)}")
    find_end_keys(instructions)