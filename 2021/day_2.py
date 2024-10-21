"""Day 2"""

from helper_functions import get_input_data


def get_position_and_depth(commands: list[str]) -> tuple[int]:
    """Returns a tuple (position, depth)."""

    position = 0
    depth = 0
    for line in commands:

        command = line.split(" ")
        direction = command[0][0]
        value = int(command[1])
        if direction == "f":
            position += value
        elif direction == "d":
            depth += value
        else:
            depth -= value

    return (position, depth)


def get_position_and_depth_with_aim(commands: list[str]) -> tuple[int]:
    """Returns (position,depth) but with aim mechanics."""

    position = 0
    depth = 0
    aim = 0

    for line in commands:

        command = line.split(" ")
        direction = command[0][0]
        value = int(command[1])
        if direction == "d":
            aim += value
        elif direction == "u":
            aim -= value
        else:
            position += value
            depth += aim * value

    return (position, depth)


def get_first_star(commands: list[str]) -> int:
    """Do the first task."""

    position, depth = get_position_and_depth(commands)
    return position * depth


def get_second_star(commands: list[str]) -> int:
    """Do the first task."""

    position, depth = get_position_and_depth_with_aim(commands)
    return position * depth


if __name__ == "__main__":

    command_list = get_input_data(2)

    print(get_first_star(command_list))
    print(get_second_star(command_list))
