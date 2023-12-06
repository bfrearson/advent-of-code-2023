from collections import namedtuple
def map_value(value, map):
    Mapping = namedtuple('Range', ['destination_range_start', 'source_range_start', 'range_length'])
    mappings = [Mapping(*(int(x) for x in line.split())) for line in map.splitlines()]
    for mapping in mappings:
        if int(value) in range(mapping.source_range_start, mapping.source_range_start + mapping.range_length) or value in range(mapping.source_range_start, mapping.source_range_start + mapping.range_length):
            return mapping.destination_range_start + int(value) - mapping.source_range_start
    return value

def map_seeds_to_location(input):
    mapping = input.split("\n\n")
    seeds = mapping[0].split(" ")[1:]
    maps = mapping[1:]
    print(mapping)
    locations = []
    for seed in seeds:
        value = int(seed)
        for map in maps:
            map = map.split(":\n")[1]
            value = map_value(value, map)
        locations.append(value)
    return locations

def map_seed_ranges_to_location(input):
    mapping = input.split("\n\n")
    split_numbers = mapping[0].split()[1:] # Split the string by whitespace to get individual numbers
    seed_pairs = [(int(split_numbers[i]), int(split_numbers[i + 1])) for i in range(0, len(split_numbers), 2)]
    seeds = [seed for range in [range(seed_pair[0], seed_pair[0]+seed_pair[1]) for seed_pair in seed_pairs] for seed in range]
    locations = []
    for seed in seeds:
        value = int(seed)
        for map in maps:
            map = map.split(":\n")[1]
            value = map_value(value, map)
        locations.append(value)
    return locations

if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        locations = map_seeds_to_location(input)
        print(f"part 1: {min(locations)}")

        # Will crash - there are billions of seeds!
        # range_locations = map_seed_ranges_to_location(input)
        # print(f"part 2: {min(range_locations)}")