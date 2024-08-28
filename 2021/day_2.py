"""Day 2"""


def get_data_from_file(filename: str) -> list[str]:
    """Gets the data from the file."""

    with open(filename, "r") as f:
        lines = f.readlines()

    return lines


def get_position_and_depth() -> tuple[int]:
    """Returns a tuple (position, depth)."""

    commands = get_data_from_file("day_2_input.txt")

    position = 0
    depth = 0
    for line in commands:

        command = line.split(" ")
        if command[0][0] == "f":
            position += int(command[1])
        elif command[0][0] == "d":
            depth += int(command[1])
        else:
            depth -= int(command[1])

    return (position, depth)


def get_first_star() -> int:
    """Do the first task."""

    position, depth = get_position_and_depth()
    return position * depth


if __name__ == "__main__":
    print(get_first_star())
