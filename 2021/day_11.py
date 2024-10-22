"""Day 11"""
from helper_functions import get_input_data, get_adjacent_points, show_grid


class DumboOctopus:
    """The abstracted version of a dumbo octopus."""

    def __init__(self, energy: int):
        """Initialisation of an octopus."""

        self.energy = energy
        self.neighbours = []
        self.already_flashed = False

    def __str__(self) -> str:
        """String representation."""

        return str(self.energy)

    def increment_energy(self):
        """Updates the energy."""

        if not self.already_flashed:

            self.energy += 1
            if self.energy > 9:
                self.flash()

    def flash(self):
        """The octopus flashes."""

        if self.energy < 10:
            raise ValueError("This octopus doesn't have enough energy.")
        if self.already_flashed:
            raise ValueError("This octopus has already flashed.")

        self.energy = 0
        self.already_flashed = True

        for neighbour in self.neighbours:
            neighbour.increment_energy()


def format_data(lines: list[str]) -> list[list[int]]:
    """Turns data into a grid of numbers."""

    return [list(map(int, list(line)))
            for line in lines]


def create_octopus_grid(number_grid) -> list[list[DumboOctopus]]:
    """Instantiates a Dumbo octopus for each number in the grid."""

    return [[DumboOctopus(energy)
             for energy in row]
            for row in number_grid]


def initialise_neighbours(grid: list[list[DumboOctopus]]) -> list[DumboOctopus]:
    """For each octopus, adds its neighbours to the object."""

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            adjacent_coords = get_adjacent_points(grid, i, j,
                                                  include_diagonals=True)
            neighbours = [grid[x][y]
                          for x, y in adjacent_coords]
            grid[i][j].neighbours = neighbours

    return grid


def take_one_step(grid: list[list[DumboOctopus]]) -> list[list[DumboOctopus]]:
    """Simulate one time step."""

    for row in grid:
        for octopus in row:
            octopus.increment_energy()

    for row in grid:
        for octopus in row:
            octopus.already_flashed = False

    return grid


def take_steps(grid: list[list[DumboOctopus]],
               steps: int) -> list[list[DumboOctopus]]:
    """Takes several steps."""

    for i in range(0, steps):
        grid = take_one_step(grid)

    return grid


if __name__ == "__main__":

    input_data = get_input_data(11, test=True)

    octogrid = create_octopus_grid(format_data(input_data))

    octogrid = initialise_neighbours(octogrid)

    octogrid = take_steps(octogrid, 100)
    show_grid(octogrid)
