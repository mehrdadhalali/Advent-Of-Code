"""Day 1"""

from helper_functions import get_input_data


def format_data(lines: list) -> list[list[int]]:
    """Returns list of list of ints, each inner list being a report."""

    return [list(map(int, line.split(" ")))
            for line in lines]


def is_it_safe(report: list[int]) -> bool:
    """Is this report safe? ie is it monotone and
     does it increase/decrease by at least 1 and at most 3?"""

    if (any(report[i] >= report[i+1]
            for i in range(0, len(report) - 1)) and
        any(report[i] <= report[i+1]
            for i in range(0, len(report) - 1))):

        return False

    if any(abs(report[i] - report[i+1]) not in range(1, 4)
           for i in range(0, len(report) - 1)):
        return False

    return True


def get_first_star(reports: list[list[int]]) -> int:
    """Does the first task."""

    return len([report for report in reports
                if is_it_safe(report)])


def remove_one_level(report: list[int], position: int) -> list[int]:
    """Removes the specified index from the list."""

    return [report[i] for i in range(0, len(report))
            if i != position]


"""TODO: There is a more efficient way to do this."""


def is_it_safe_with_dampener(report: list[int]) -> bool:
    """Is the report safe with a dampener? ie does removing a single
        level make it safe?"""

    return is_it_safe(report) or any(is_it_safe(remove_one_level(report, i))
                                     for i in range(0, len(report)))


def get_second_star(reports: list[list[int]]) -> int:
    """Does the second task."""

    return len([report for report in reports
                if is_it_safe_with_dampener(report)])


if __name__ == "__main__":

    input_data = get_input_data(2, False)

    unusual_reports = format_data(input_data)

    print(get_second_star(unusual_reports))
