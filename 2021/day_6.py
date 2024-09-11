"""Day 6"""
from read_from_file import get_input_data


def format_data(txt_data: list[str]) -> list[int]:
    """Turns the data into a list of integers."""

    return list(map(int, txt_data[0].split(",")))


"""
The output of the function below is the sequence with the following recurrence relation:
c(n) = 1 for  1<=n<=8,
c(n) = c(n-9) + c(n-7) for n>8
"""


def num_lanternfish(days: int) -> int:
    """Returns the number of lanternifish that would exist after a number of days,
        assuming we started from 1 newborn lanternfish."""

    if days < 8:
        return 1

    lanternfish_in_day = [1] * days

    for i in range(8, days):
        lanternfish_in_day[i] = lanternfish_in_day[i-7] + \
            lanternfish_in_day[i-9]

    return lanternfish_in_day[-1]


def get_first_star(fish_data: list[int]) -> int:
    """Gets the first task done."""

    num_days = 80

    return sum([num_lanternfish(8+num_days-n) for n in fish_data])


def get_second_star(fish_data: list[int]) -> int:
    """Gets the second task done."""

    num_days = 256

    """The following line still works:
        return sum([num_lanternfish(8+num_days-n) for n in fish_data])
        and it still solves the problem quite quickly.
        However, it can be made even more efficient.
        For every entry in the input, we only need to solve it once.
        Afterwards, we can keep it in memory.
    """

    timer_to_fish = [num_lanternfish(7+num_days-i)
                     for i in range(0, 5)]

    return sum([timer_to_fish[n-1] for n in fish_data])


if __name__ == "__main__":

    data = get_input_data(6)
    data = format_data(data)

    print(get_first_star(data))

    print(get_second_star(data))
