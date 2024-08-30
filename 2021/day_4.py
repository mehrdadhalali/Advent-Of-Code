"""Day 4"""
from read_from_file import get_input_data


def get_bingo_inputs(line: str) -> list[int]:
    """Returns a list of bingo inputs."""

    bingo_inputs_char = line.split(",")
    return list(map(int, bingo_inputs_char))


def get_bingo_board(board_lines: list[str]) -> list[list[int]]:
    """Returns a Bingo board."""

    for i in range(0, len(board_lines)):
        board_lines[i] = [int(num) for num in board_lines[i].split(" ")
                          if num != '']

    return board_lines


def format_data(lines: list[str]) -> list:
    """Formats the data into
        - A list of integers (Bingo inputs)
        - A list of grids (player boards)"""

    # Remove whitespace
    inputs = [line for line in lines if line != '']

    bingo_inputs = get_bingo_inputs(inputs[0])

    for i in range(0, (len(inputs)-1)//5):
        # TODO: instead of print, instantiate a player per board
        print(get_bingo_board(inputs[5*i+1: 5*i+6]))


if __name__ == "__main__":
    input_data = get_input_data(4)

    format_data(input_data)
