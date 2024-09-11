"""Day 6"""
from read_from_file import get_input_data


def format_data(txt_data: list[str]) -> list[int]:
    """Turns the data into a list of integers."""

    return list(map(int, txt_data[0].split(",")))


def num_lanternfish(days: int = 80) -> int:
    """Returns the number of lanternifish that would exist after a number of days,
        assuming we started from 1 newborn lanternfish."""

    if days < 9:
        return 1

    return num_lanternfish(days-9) + num_lanternfish(days-7)


def get_first_star(fish_data: list[int]) -> int:

    num_days = 80

    return sum([num_lanternfish(8+num_days-n) for n in fish_data])


# TODO: Change num_lanternfish to a dynamic algorithm for efficiency
if __name__ == "__main__":

    data = get_input_data(6)
    data = format_data(data)

    print(get_first_star(data))

    num_of_days = 256

    print(num_lanternfish(num_of_days))
