"""Day 7"""
from read_from_file import get_input_data


def format_data(data: str) -> list[int]:
    """Turns data into a sorted list of numbers and their count."""

    list_ints = sorted(list(map(int, data.split(","))))

    return list_ints


def compare_right(numbers: list[int], number: int) -> bool:
    """Returns true if all numbers on the right, including the input number are the majority."""

    less_than_or_equal_to = len([num for num in numbers if num <= number])

    if less_than_or_equal_to >= len(numbers)//2:
        return True

    return False


def calculate_fuel(numbers: list[int], number: int) -> int:
    """Calculates the fuel needed for all crabs to move to a certain position."""

    return sum([abs(num - number) for num in numbers])


def get_first_star(data: list[str]) -> int:
    """Does the first task."""

    numbers = format_data(data[0])

    current_guess = min(numbers)

    while not compare_right(numbers, current_guess):
        current_guess += 1

    return calculate_fuel(numbers, current_guess)


if __name__ == "__main__":

    input_data = get_input_data(7)

    print(get_first_star(input_data))
