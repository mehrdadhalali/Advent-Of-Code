"""Day 5"""

from helper_functions import get_input_data
from helper_classes import Grid

def format_data(lines: list) -> dict:
    """Return the data as a dictionary."""

    break_index = lines.index("")
    return {"ranges": [(int(line.split("-")[0]), int(line.split("-")[1])) for line in lines[:break_index]],
            "ids": list(map(int, lines[break_index + 1:]))}


def create_mutually_exclusive_ranges(ranges: list) -> list:
    """Merge overlapping ranges so that they're all mustually exclusive."""

    ranges.sort(key = lambda rng: rng[0])
    i = 0
    while i < len(ranges) - 1:

        if ranges[i][1] >= ranges[i+1][0]:
            new_lower = ranges[i][0]
            new_upper = max(ranges[i+1][1], ranges[i][1])
            ranges = ranges[:i] + [(new_lower, new_upper)] + ranges[i+2:]
        else:
            i += 1

    return ranges


def find_fresh_ids(id_data: dict) -> list:
    """Find the fresh IDs in the now-mutually-exlusive ranges"""

    ranges, ids = id_data["ranges"], id_data["ids"]
    range_index = 0
    fresh_ids = []

    for id in ids:
        while id > ranges[range_index][1]:
            range_index += 1
            if range_index == len(ranges):
                return fresh_ids
        for range in ranges[range_index:]:
            if id > range[0]:
                fresh_ids.append(id)
                break
    
    return fresh_ids

            



def get_first_star(id_data: dict) -> int:
    """Does the first task."""

    return len(find_fresh_ids(id_data))
            


def get_second_star(ranges: list) -> int:
    """Does the second task."""

    ranges = create_mutually_exclusive_ranges(ranges)
    return sum([range[1] - range[0] + 1 for range in ranges])

if __name__ == "__main__":
    
    id_data = format_data(get_input_data(5, False))
    id_data["ranges"] = create_mutually_exclusive_ranges(id_data["ranges"])
    id_data["ids"].sort()

    print(get_first_star(id_data))
    print(get_second_star(id_data["ranges"]))


    