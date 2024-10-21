"""Day 5"""
from helper_functions import get_input_data


def format_line(line: str) -> tuple[tuple[int]]:
    """Turns "a,b -> c,d" into ((a, b), (c, d)). """

    return tuple([tuple(map(int, coords.split(","))) for coords in line.split("->")])


def format_text_data(text: list[str]) -> list[tuple[tuple[int]]]:
    """Formats the entire text file into a list of lines."""

    return [format_line(line) for line in text]


def is_hor_or_ver(line: tuple[tuple[int]]) -> bool:
    """Is this line horizontal/vertical?"""

    return line[0][0] == line[1][0] or line[0][1] == line[1][1]


def get_points(line: tuple[tuple[int]]) -> set[tuple[int]]:
    """ Given the start and the end of a line, returns the set of all integer points on that line.
        Note: The line MUST be horizontal or vertical. """

    line_start = line[0]
    line_end = line[1]

    # Base case
    if line_start == line_end:
        return {line_start}

    delta_x = 0
    delta_y = 0

    if line_start[0] < line_end[0]:
        delta_x = 1
    elif line_start[0] > line_end[0]:
        delta_x = -1

    if line_start[1] < line_end[1]:
        delta_y = 1
    elif line_start[1] > line_end[1]:
        delta_y = -1

    return {line_start}.union(get_points(((line_start[0]+delta_x,
                                          line_start[1]+delta_y),
                                         line_end)))


def get_points_of_intersection(lines: list[set]) -> set:
    """Returns a set of all of the points of intersection of the lines."""

    n = len(lines)

    points_of_intersection = set({})

    for i in range(0, n-1):
        for j in range(i+1, n):
            points = set((lines[i]).intersection(lines[j]))
            points_of_intersection = points_of_intersection.union(points)

    return points_of_intersection


def calculate_points_of_intersection(text_data: list[str], task_no: int) -> int:
    """The main function."""

    lines = format_text_data(text_data)

    if task_no == 1:
        lines = [line for line in lines if is_hor_or_ver(line)]

    line_points = [get_points(line) for line in lines]

    return len(get_points_of_intersection(line_points))


def get_first_star(text_data: list[str]) -> int:
    """Completes task 1."""

    return calculate_points_of_intersection(text_data, 1)


def get_second_star(text_data: list[str]) -> int:
    """Completes task 2."""

    return calculate_points_of_intersection(text_data, 2)


if __name__ == "__main__":

    data = get_input_data(5)

    print(get_first_star(data))
    print(get_second_star(data))
