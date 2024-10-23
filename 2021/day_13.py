"""Day 13"""

from helper_functions import get_input_data, show_grid, transpose


def format_coordinates(coordinate_strings: list[str]) -> list[tuple[int]]:
    """Formats the coordinates."""

    return [(int(element.split(",")[0]),
             int(element.split(",")[1]))
            for element in coordinate_strings]


def format_instructions(instruction_strings: list[str]) -> list[dict]:
    """Formats the instructions."""

    instructions = []
    for line in instruction_strings:
        instructions.append({
            "axis": line[11],
            "value": int(line[13:])
        })

    return instructions


def format_data(data: list[str]) -> dict:
    """Formats the data properly."""

    separator = data.index("")
    coordinate_strings = data[:separator]
    instruction_strings = data[separator+1:]

    coordinates = format_coordinates(coordinate_strings)
    instructions = format_instructions(instruction_strings)

    return {
        "coordinates": coordinates,
        "instructions": instructions
    }


def find_grid_dimensions(coordinates: list[tuple[int]]) -> dict:
    """Returns the dimensions that the grid must have."""

    max_rows = max([coord[1] for coord in coordinates]) + 1
    max_columns = max([coord[0] for coord in coordinates]) + 1

    return {
        "rows": max_rows,
        "columns": max_columns
    }


def create_grid(coordinates: list[tuple[int]],
                dimensions: dict) -> list[list[int]]:
    rows, columns = dimensions["rows"], dimensions["columns"]

    one_row = [0]*columns
    grid = [one_row.copy() for i in range(0, rows)]

    for coords in coordinates:
        grid[coords[1]][coords[0]] = 1

    return grid


def superimpose_rows(row_1: list[int], row_2: list[int]) -> list[int]:
    """Superimposes 2 rows."""

    return [row_1[i] | row_2[i]
            for i in range(0, len(row_1))]


def fold_grid_vertically(grid: list[list[int]], fold_index: int) -> list[list[int]]:
    """Folds a grid vertically."""

    for i in range(0, fold_index):
        grid[i] = superimpose_rows(grid[i], grid[2*fold_index - i])

    return grid[0: fold_index + 1]


def fold_grid_horizontally(grid: list[list[int]], fold_index: int) -> list[list[int]]:
    """Folds a grid horizontally."""

    return transpose(fold_grid_vertically(transpose(grid), fold_index))


def fold_grid(grid: list[list[int]], axis: str, fold_index: int) -> list[list[int]]:
    """Folds a grid properly."""

    if axis == "y":
        return fold_grid_vertically(grid, fold_index)

    if axis == "x":
        return fold_grid_horizontally(grid, fold_index)

    raise ValueError("Invalid axis parameter!")


def count_ones(grid: list[list[int]]) -> int:
    """How many 1s are there in this grid?"""

    return len([element for row in grid
                for element in row
                if element == 1])


def get_first_star(data: dict) -> int:
    """Does the first task."""

    coordinates = data["coordinates"]
    instructions = data["instructions"]

    grid = create_grid(coordinates, find_grid_dimensions(coordinates))

    fold_instructions = instructions[0]

    grid = fold_grid(grid, fold_instructions["axis"],
                     fold_instructions["value"])

    return count_ones(grid)


def make_more_visible(grid: list[list[int]]) -> list[list[str]]:
    """Currently, the letters in the grid are hard to see.
        This function formats it like they are on the website."""

    bit_map = [".", "#"]

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            grid[i][j] = bit_map[grid[i][j]]
    return grid


def get_second_star(data: dict) -> None:
    """Does the second task."""

    coordinates = data["coordinates"]
    instructions = data["instructions"]

    grid = create_grid(coordinates, find_grid_dimensions(coordinates))

    for instruction in instructions:
        grid = grid = fold_grid(grid, instruction["axis"],
                                instruction["value"])

    show_grid(make_more_visible(grid))


if __name__ == "__main__":

    input_data = get_input_data(13, test=False)

    formatted_data = format_data(input_data)

    print(get_first_star(formatted_data))
    get_second_star(formatted_data)
