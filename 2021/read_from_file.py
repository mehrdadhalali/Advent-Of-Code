"""This script is for reading data from input files."""


def get_input_data(day_number: int) -> list:
    """Gets the lines from the input file."""

    with open(f"day_{day_number}_input.txt", "r") as f:
        lines = f.readlines()

    return lines
