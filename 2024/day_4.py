"""Day 4"""

from helper_functions import get_input_data
from helper_classes import Grid


def format_data(lines: list[str]) -> list[list[str]]:
    """Turns the data into a grid of ints."""

    return Grid([list(line) for line in lines])


def find_xmas_count_in_line(line: list[str]) -> int:
    """Finds the number of times XMAS appears in a line."""

    xmas_count = 0

    for i in range(0, len(line) - 3):
        if "".join(line[i:i+4]) in ["XMAS", "SAMX"]:
            xmas_count += 1

    return xmas_count


def find_xmas_horizontal(grid: list[list[str]]) -> int:
    """Finds the number of times XMAS is in the rows."""

    return sum([find_xmas_count_in_line(row)
                for row in grid])


def find_xmas_vertical(grid: list[list[str]]) -> int:
    """Finds the number of times XMAS is in the columns."""

    grid_transposed = [[grid[j][i] for j in range(0, len(grid))]
                       for i in range(0, len(grid[0]))]

    return find_xmas_horizontal(grid_transposed)


def get_pos_line(grid: list[list[str]], start_row: int, start_col: int) -> list[int]:
    """Returns a line in the grid with gradient 1, starting from a given point."""

    col_max = len(grid[0])

    line = []

    row = start_row
    col = start_col

    while row >= 0 and col < col_max:
        line.append(grid[row][col])
        row -= 1
        col += 1

    return line


def get_all_pos_lines(grid: list[list[str]]) -> list[list[str]]:
    """Returns all diagonal lines of positive gradient, with length > 3."""

    start_coords = [(i, 0) for i in range(3, len(grid))]
    start_coords.extend([(len(grid) - 1, j) for j in range(1, len(grid[0])-3)])

    return [get_pos_line(grid, coord[0], coord[1])
            for coord in start_coords]


def get_neg_line(grid: list[list[str]], start_row: int, start_col: int) -> list[int]:
    """Returns a line in the grid with gradient -1, starting from a given point."""

    col_max = len(grid[0])
    row_max = len(grid)

    line = []

    row = start_row
    col = start_col

    while row < row_max and col < col_max:
        line.append(grid[row][col])
        row += 1
        col += 1

    return line


def get_all_neg_lines(grid: list[list[str]]) -> list[list[str]]:
    """Returns all diagonal lines of positive gradient, with length > 3."""

    start_coords = [(0, i) for i in range(0, len(grid[0])-3)]
    start_coords.extend([(j, 0) for j in range(1, len(grid)-3)])

    return [get_neg_line(grid, coord[0], coord[1])
            for coord in start_coords]


def get_first_star(grid: list[list[str]]) -> int:
    """Does the first task."""

    xmas_hor = find_xmas_horizontal(grid)
    xmas_ver = find_xmas_vertical(grid)
    xmas_diag_pos = find_xmas_horizontal(get_all_pos_lines(grid))
    xmas_diag_neg = find_xmas_horizontal(get_all_neg_lines(grid))

    return xmas_hor + xmas_ver + xmas_diag_pos + xmas_diag_neg


def get_3_by_3_block(grid: list[list[str]], row_coord: int, col_coord: int) -> list[list[str]]:
    """Takes out a 3x3 block whose top left corner is specified."""

    if row_coord > len(grid) - 3 or col_coord > len(grid[0]) - 3:
        raise ValueError("You're going out of the grid!")

    return [grid[i][col_coord:col_coord+3]
            for i in range(row_coord, row_coord+3)]


def is_it_x_mas(block: list[list[str]]) -> bool:
    """Is this 3x3 block a X-MAS block?"""

    neg_line = "".join([block[i][i] for i in range(0, 3)])
    pos_line = "".join([block[i][2 - i] for i in range(0, 3)])

    mas = ["MAS", "SAM"]

    return (neg_line in mas) and (pos_line in mas)


def get_all_blocks(grid: list[list[str]]) -> list[list[list[str]]]:
    """Returns all 3x3 blocks."""

    return [get_3_by_3_block(grid, i, j) for i in range(0, len(grid) - 2)
            for j in range(0, len(grid[0]) - 2)]


def get_second_star(grid: list[list[str]]) -> int:
    """Does the second task."""

    blocks = get_all_blocks(grid)

    return sum([is_it_x_mas(block) for block in blocks])


if __name__ == "__main__":

    input_data = get_input_data(4, False)
    grid = format_data(input_data).grid

    print(get_first_star(grid))
    print(get_second_star(grid))
