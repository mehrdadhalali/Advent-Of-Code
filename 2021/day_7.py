"""Day 7"""
from helper_functions import get_input_data


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


def calculate_fuel(numbers: list[int], position: int) -> int:
    """Calculates the fuel needed for all crabs to move to a certain position."""

    return sum([abs(num - position) for num in numbers])


def triangular(n: int) -> int:
    """Calculates sum of 1 to n."""

    return n*(n+1)//2


def calculate_fuel_2(numbers: list[int], position: int) -> int:
    """Calculates the fuel needed for all crabs to move to a certain position, according to Task 2."""

    return sum([triangular(abs(num - position)) for num in numbers])


def calculate_profit(numbers: list[int], new_position: int) -> int:
    """Given a list of numbers, calculates the fuel we save if we jumped on the first number from its left,
        It uses the fuel formula of task 2."""

    return sum([number - new_position + 1 for number in numbers])


def calculate_loss(numbers: list[int], old_position: int) -> int:
    """Given a list of numbers, calculates the fuel added if we jumped from the last number, to the right,
    it uses the fuel formula of task 2."""

    return sum([old_position - number + 1 for number in numbers])


def decide_jump(numbers: list[int], current_point: int) -> bool:
    """Should we jump to the right?"""

    cost_list = [number for number in numbers if number <= current_point]
    profit_list = [number for number in numbers if number > current_point]

    if calculate_profit(profit_list, current_point + 1) > calculate_loss(cost_list, current_point):
        return True

    return False


def get_first_star(numbers: list[int]) -> int:
    """Does the first task."""

    current_guess = numbers[0]

    while not compare_right(numbers, current_guess):
        current_guess += 1

    return calculate_fuel(numbers, current_guess)


def get_second_star(numbers: list[int]) -> int:
    """Does the second task."""

    current_guess = numbers[0]

    while decide_jump(numbers, current_guess):
        current_guess += 1

    return calculate_fuel_2(numbers, current_guess)


if __name__ == "__main__":

    input_data = get_input_data(7)

    input_numbers = format_data(input_data[0])

    print(get_first_star(input_numbers))
    print(get_second_star(input_numbers))
