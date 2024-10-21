"""Day 9"""
from helper_functions import get_input_data


def format_data(lines: list[str]) -> list[list[str]]:
    """Formats the data into a grid."""

    grid_str = list(map(list, lines))

    return [list(map(int, line)) for line in grid_str]


# TODO: put guards in the grid, filled with "-1" instead
def get_adjacent_points(grid: list[list], row: int, column: int) -> list[int]:
    """Returns the coordinates of all of the adjacent points to a point."""

    num_rows = len(grid)
    num_cols = len(grid[0])

    adjacent_coordinates = [(row+1, column),
                            (row - 1, column),
                            (row, column + 1),
                            (row, column - 1)]
    adjacent_points = []

    for coord in adjacent_coordinates:
        if coord[0] in range(0, num_rows) and coord[1] in range(0, num_cols):
            adjacent_points.append(coord)

    return adjacent_points


def make_basins(grid: list[list[int]]) -> list[list[int]]:
    """Turns every number that isn't 9 into a 0, 
        hence revealing the basins (0s) that are separated by the walls (9s)."""

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] != 9:
                grid[i][j] = 0

    return grid


def find_basin(grid: list[list[int]], point: tuple[int]) -> set[tuple[int]]:
    """Finds a basin in the grid, given a point of that basin."""

    basin_points = set([])
    to_search = [point]

    while len(to_search) > 0:
        current_point = to_search.pop(0)

        adjacent_points = get_adjacent_points(
            grid, current_point[0], current_point[1])
        to_search += [point for point in adjacent_points
                      if grid[point[0]][point[1]] == 0]

        basin_points = basin_points.union({current_point})
        grid[current_point[0]][current_point[1]] = 1

    return basin_points


def get_next_basin_start(grid: list[list[int]]) -> tuple[int]:
    """Returns the next unexplored point of the grid."""

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)

    return (-1, -1)


def get_first_star(grid: list[list[int]]) -> int:
    """Does the first task."""

    low_points = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            point = grid[i][j]
            adjacent_points = get_adjacent_points(grid, i, j)
            if all(point < grid[coord[0]][coord[1]]
                   for coord in adjacent_points):
                low_points.append(point + 1)

    return sum(low_points)


def get_second_star(grid: list[list[int]]) -> int:
    """Does the second task."""

    grid = make_basins(grid)

    basin_sizes = []

    while get_next_basin_start(grid)[0] != -1:
        starting_point = get_next_basin_start(grid)
        basin_sizes.append(len(find_basin(grid, starting_point)))

    basin_sizes.sort(reverse=True)
    return basin_sizes[0]*basin_sizes[1]*basin_sizes[2]


def show_grid(grid: list[list[int]]) -> None:
    """Function that helps visualise the grid."""

    for row in grid:
        print("".join(list(map(str, row))))


if __name__ == "__main__":

    input_data = get_input_data(9)

    grid = format_data(input_data)

    print(get_first_star(grid))
    print(get_second_star(grid))
