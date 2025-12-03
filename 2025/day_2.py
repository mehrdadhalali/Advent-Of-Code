"""Day 2"""

from helper_functions import get_input_data

def format_data(lines: list) -> list[tuple]:
    """Return the instruction in a list of tuples."""

    return [tuple(map(int, entry.split("-"))) for entry in lines[0].split(",")]

def is_id_invalid_1(id_num: int) -> bool:
    """Is the ID invalid according to part 1?"""

    num_str = str(id_num)
    length = len(num_str)
    if length % 2 == 1:
        return False
    
    return num_str[:(length//2)] == num_str[(length//2):]

def is_id_invalid_2(id_num: int) -> bool:
    """Is the ID invalid according to part 2?"""

    num_str = str(id_num)
    length = len(num_str)
    for i in range(1, length):
        if length % i != 0:
            continue
        substring = num_str[:i]
        if num_str.count(substring) == length // len(substring):
            return True
    
    return False


def get_first_star(id_ranges: list) -> int:
    """Does the first task."""

    invalid_sum = 0
    for id_range in id_ranges:
        for number in range(id_range[0], id_range[1] + 1):
            if is_id_invalid_1(number):
                invalid_sum += number

    return invalid_sum

def get_second_star(id_ranges: list) -> int:
    """Does the second task."""

    invalid_sum = 0
    for id_range in id_ranges:
        for number in range(id_range[0], id_range[1] + 1):
            if is_id_invalid_2(number):
                invalid_sum += number

    return invalid_sum

if __name__ == "__main__":
    
    id_ranges = format_data(get_input_data(2, False))

    print(get_second_star(id_ranges))

