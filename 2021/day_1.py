"""Day 1"""
from helper_functions import get_input_data


def num_larger_than_prev(measurements: list) -> int:
    """Returns the number of measurements larger than the last."""

    total = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            total += 1

    return total


def three_measure_window_larger_than_prev(measurements: list) -> int:
    """Returns the number of three-window measurements larger than the last."""

    total = 0
    for i in range(0, len(measurements)-3):
        if measurements[i] < measurements[i+3]:
            total += 1

    return total


def get_first_star(measurements: list) -> int:
    """Completes the first task."""

    return num_larger_than_prev(measurements)


def get_second_star(measurements: list) -> int:
    """COmpleted the second task."""

    return three_measure_window_larger_than_prev(measurements)


if __name__ == "__main__":

    input_measurements = [int(line) for line in get_input_data(1)]

    print(get_first_star(input_measurements))
    print(get_second_star(input_measurements))
