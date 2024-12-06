"""Day 6"""

from helper_functions import get_input_data
from helper_classes import Grid


class MappedArea(Grid):
    """A grid that also keeps track of traversed coordinates.
        The list "traversed" has elements of the form:
        (position, direction). We only need the position for challenge 1,
        but for challenge 2, direction also comes in handy. """

    def __init__(self, grid: list[list]):
        super().__init__(grid)
        self.traversed = []
        guard_position = [(i, j) for i in range(0, self.rows)
                          for j in range(0, self.columns)
                          if self.grid[i][j] == "^"]
        if len(guard_position) != 1:
            raise ValueError("There should be exactly one guard!")
        self.traversed.append((guard_position[0], (-1, 0)))


def format_data(lines: list) -> MappedArea:
    """Turns data into a Mapped Area"""

    area_grid = [list(line) for line in lines]

    return MappedArea(area_grid)


def rotate_right(direction: tuple[int]) -> tuple[int]:
    """Rotates the direction 90 degrees clockwise."""

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    index = dirs.index(direction)

    return dirs[(index + 1) % 4]


def take_one_step(area: MappedArea) -> dict:
    """Takes one time step, given direction."""

    guard_pos, direction = area.traversed[-1]

    end = False
    loop = False

    new_pos = (guard_pos[0] + direction[0],
               guard_pos[1] + direction[1])

    if not area.contains(new_pos):
        end = True

    elif area.loc(new_pos) == "#":

        direction = rotate_right(direction)

        if (guard_pos, direction) in area.traversed:
            loop = True

        area.traversed.append((guard_pos, direction))

    else:

        if (new_pos, direction) in area.traversed:
            loop = True

        area.traversed.append((new_pos, direction))

    return {
        "area": area,
        "end": end,
        "loop": loop
    }


def run_simulation(area: MappedArea) -> str:
    """Runs the simulation, returns "end" or "loop"."""

    end = False
    loop = False

    while not (end or loop):

        results = take_one_step(area)
        end = results["end"]
        loop = results["loop"]

    return "end" if end else "loop"


def get_first_star(area: MappedArea) -> int:
    """Does the first task."""

    result = run_simulation(area)

    if result != "end":
        raise ValueError("Simulation should always end in challenge 1!")

    return len(set([t[0] for t in area.traversed]))

# TODO: This is incredibly inefficient, takes about 15 mins, find a better way


def get_second_star(area: MappedArea) -> int:
    """Does the second task."""

    initial_run = run_simulation(area)
    guards_path = list(set([t[0] for t in area.traversed]))
    area.traversed = [area.traversed[0]]

    loops = 0
    count = 0

    for (i, j) in guards_path:
        if area.loc((i, j)) == ".":
            count += 1
            if count == 93:
                print(count)
            area.grid[i][j] = "#"
            if run_simulation(area) == "loop":
                loops += 1

            area.grid[i][j] = "."
            area.traversed = [area.traversed[0]]

    return loops


if __name__ == "__main__":

    input_data = get_input_data(6, test=False)

    mapped_area = format_data(input_data)

    print(get_second_star(mapped_area))
