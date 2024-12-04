"""Day 3"""

import re

from helper_functions import get_input_data


def format_data(lines: list) -> str:
    """Returns a single string, as the lines don't matter."""

    return "".join(lines)


def perform_multiplication(mult_str: str) -> int:
    """Performs a multiplication in the form mul(x,y)."""

    numbers = list(map(int, mult_str[4:-1].split(",")))

    return numbers[0] * numbers[1]


def get_first_star(memory: str) -> int:
    """Does the first task."""

    valid_instructions = re.findall("mul\(\d*,\d*\)", memory)

    return sum([perform_multiplication(mult) for mult in valid_instructions])


def process_dont_chunk(chunk: str) -> int:
    """Finds the first "do" command, evaluates everything after it."""

    start_from = re.search("do", chunk)

    if start_from is None:
        return 0

    return get_first_star(chunk[start_from.span()[1]:])


def get_second_star(memory: str) -> int:
    """Does the second task."""

    dont_chunks = re.split("don't", corrupted_memory)

    first_bit = get_first_star(dont_chunks[0])

    if len(dont_chunks) == 1:
        return first_bit

    else:
        return first_bit + sum([process_dont_chunk(dont_chunk)
                               for dont_chunk in dont_chunks[1:]])


if __name__ == "__main__":

    input_data = get_input_data(3, test=False)

    corrupted_memory = format_data(input_data)

    print(get_first_star(corrupted_memory))
    print(get_second_star(corrupted_memory))
