"""Day 8"""

from helper_functions import get_input_data
from helper_classes import Grid


def format_data(lines: list) -> Grid:
    """Returns a grid."""

    area_grid = [list(line) for line in lines]

    return Grid(area_grid)


def get_antenna_coords(antennas: Grid) -> dict:
    """Returns a dictionary of the following format:
        {antenna: [(x,y)]}"""

    coords = {}
    for i in range(0, antennas.rows):
        for j in range(0, antennas.columns):
            value = antennas.loc((i, j))
            if value != ".":
                antenna_coords = coords.get(value, [])
                antenna_coords.append((i, j))
                coords[value] = antenna_coords

    return coords


def generate_antinode_pair(a: tuple[int], b: tuple[int]) -> list:
    """Given a pair of coordinates, returns a pair of antinode locations."""

    vector = (b[0] - a[0], b[1] - a[1])

    return [(b[0]+vector[0], b[1]+vector[1]),
            (a[0]-vector[0], a[1]-vector[1])]


def create_antinodes_for_antenna(coords: list, harmonic: bool, grid: Grid) -> list:
    """Given a list of coords for one antenna, create all antinodes."""

    antinodes = []
    for i in range(0, len(coords) - 1):
        for j in range(i+1, len(coords)):
            if not harmonic:
                antinodes.extend(generate_antinode_pair(coords[i], coords[j]))
            else:
                antinodes.extend(
                    generate_resonant_harmonic_from_pair(coords[i], coords[j], grid))

    return antinodes


def create_all_antinodes(antenna_dict: dict, grid: Grid, harmonic: bool = False) -> list:
    """Generate every single antinode, whether or not is't in the grid."""

    all_antinodes = []
    for key in antenna_dict.keys():
        antennas = antenna_dict[key]
        all_antinodes.extend(
            create_antinodes_for_antenna(antennas, harmonic, grid))

    if not harmonic:
        all_antinodes = [antinode for antinode in all_antinodes
                         if grid.contains(antinode)]
    return list(set(all_antinodes))


def get_first_star(grid: Grid) -> int:
    """Does the first task."""

    antenna_dict = get_antenna_coords(grid)

    return len(create_all_antinodes(antenna_dict, grid))


def generate_resonant_harmonic_from_pair(a: tuple[int], b: tuple[int], grid: Grid) -> list:
    """Given two points, returns all points on a line they make in a lattice,
        as long as it's in the grid's bounds."""

    vector = (b[0] - a[0], b[1] - a[1])
    antinodes = []

    current_pos = b
    while grid.contains(current_pos):
        antinodes.append(current_pos)

        current_pos = (current_pos[0] + vector[0],
                       current_pos[1] + vector[1])

    current_pos = a
    while grid.contains(current_pos):
        antinodes.append(current_pos)

        current_pos = (current_pos[0] - vector[0],
                       current_pos[1] - vector[1])

    return antinodes


def get_second_star(grid: Grid) -> int:
    """Does the second task."""

    antenna_dict = get_antenna_coords(grid)

    return len(create_all_antinodes(antenna_dict, grid, True))


if __name__ == "__main__":

    input_data = get_input_data(8, test=False)

    antenna_map = format_data(input_data)

    print(get_first_star(antenna_map))
    print(get_second_star(antenna_map))
