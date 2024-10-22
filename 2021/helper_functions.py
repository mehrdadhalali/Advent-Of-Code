"""This script is for useful functions that are handy in different scripts."""


def get_input_data(day_number: int, test: bool = False) -> list:
    """Gets the lines from the input file."""

    if test:
        file_name = f"inputs/test_day_{day_number}_input.txt"
    else:
        file_name = f"inputs/day_{day_number}_input.txt"

    with open(file_name, "r") as f:
        lines = (f.read()).split("\n")

    return lines

# TODO: put guards in the grid, filled with "-1" instead


def get_adjacent_points(grid: list[list], row: int, column: int,
                        include_diagonals: bool = False) -> list[tuple[int]]:
    """Returns the coordinates of all of the adjacent points to a point."""

    num_rows = len(grid)
    num_cols = len(grid[0])

    adjacent_coordinates = [(row+1, column),
                            (row - 1, column),
                            (row, column + 1),
                            (row, column - 1)]

    if include_diagonals:
        adjacent_coordinates.extend([(row+1, column+1),
                                     (row+1, column-1),
                                     (row-1, column+1),
                                     (row-1, column-1)])

    adjacent_points = []

    for coord in adjacent_coordinates:
        if coord[0] in range(0, num_rows) and coord[1] in range(0, num_cols):
            adjacent_points.append(coord)

    return adjacent_points


def show_grid(grid: list[list]) -> None:
    """Function that helps visualise the grid."""

    for row in grid:
        print("".join(list(map(str, row))))
