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

if __name__ == "__main__":
    with open("input.txt") as input:
        locations = map_seeds_to_location(input.read())
        print(min(locations))