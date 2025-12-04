"""Day 4"""

from helper_functions import get_input_data
from helper_classes import Grid

def format_data(lines: list) -> list[tuple]:
    """Return the data as a list of list of numbers."""

    return Grid([list(line) for line in lines])

def remove_accessible_rolls(rolls: Grid) -> int:
    """Removes accessible rolls (<4 adjacent rolls) and returns the number of rolls removed."""

    accessible_rolls = []
    for i in range(0, rolls.rows):
        for j in range(0, rolls.columns):
            if rolls.loc((i,j)) == "@":
                adjacent_coords = rolls.get_adjacent_points(i, j, include_diagonals= True)
                adjacent_roll_count = [rolls.loc(coord) for coord in adjacent_coords].count("@")
                if adjacent_roll_count < 4:
                    accessible_rolls.append((i, j))

    for coordinate in accessible_rolls:
        rolls.grid[coordinate[0]][coordinate[1]] = "."

    return len(accessible_rolls)

def get_first_star(rolls: Grid) -> int:
    """Does the first task."""
    
    return remove_accessible_rolls(rolls)
            


def get_second_star(rolls: Grid) -> int:
    """Does the second task."""

    rolls_removed = 0
    while True:
        rolls_removed_per_step = remove_accessible_rolls(rolls)
        if rolls_removed_per_step == 0:
            break
        rolls_removed += rolls_removed_per_step
    return rolls_removed

if __name__ == "__main__":
    
    rolls = format_data(get_input_data(4, False))
    print(get_second_star(rolls))