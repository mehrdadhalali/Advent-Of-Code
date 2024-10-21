"""Day 11"""
from helper_functions import get_input_data


class DumboOctopus:
    """The abstracted version of a dumbo octopus."""

    def __init__(self, energy: int):

        self.energy = energy
        self.neighbours = []


def format_data(lines: list[str]) -> list[list[int]]:
    """Turns data into a grid of numbers."""

    return [list(map(int, list(line)))
            for line in lines]


def create_octopus_grid(number_grid) -> list[list[DumboOctopus]]:
    """Instantiates a Dumbo octopus for each number in the grid."""

    return [[DumboOctopus(energy)
             for energy in row]
            for row in number_grid]


if __name__ == "__main__":

    input_data = get_input_data(11)
    print(format_data(input_data))
