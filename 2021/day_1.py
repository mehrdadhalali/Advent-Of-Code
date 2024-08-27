"""Day 1"""


def get_data_from_file(filename: str) -> list[str]:
    """Gets the data from the file."""

    with open(filename, "r") as f:
        lines = f.readlines()

    return [int(line) for line in lines]


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


def get_first_star() -> int:
    """Completes the first task."""

    measurements = get_data_from_file("day_1_input.txt")
    return num_larger_than_prev(measurements)


def get_second_star() -> int:
    """COmpleted the second task."""

    measurements = get_data_from_file("day_1_input.txt")
    return three_measure_window_larger_than_prev(measurements)


if __name__ == "__main__":

    print(get_first_star())
    print(get_second_star())
