"""This script is for reading data from input files."""


def get_input_data(day_number: int, test: bool = False) -> list:
    """Gets the lines from the input file."""

    if test:
        file_name = f"inputs/test_day_{day_number}_input.txt"
    else:
        file_name = f"inputs/day_{day_number}_input.txt"

    with open(file_name, "r") as f:
        lines = (f.read()).split("\n")

    return lines
