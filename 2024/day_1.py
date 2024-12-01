"""Day 1"""

from helper_functions import get_input_data


def format_data(lines: list) -> tuple[list]:
    """Returns a tuple of lists, for each list of IDs."""

    first_ids = []
    second_ids = []

    for line in lines:
        ids = line.split("   ")

        first_ids.append(int(ids[0]))
        second_ids.append(int(ids[1]))

    return first_ids, second_ids


def calculate_distance(first_ids: list[int], second_ids: list[int]) -> int:
    """Calculates the distance between the two lists."""

    return sum([abs(first_ids[i] - second_ids[i]) for i in range(0, len(first_ids))])


def get_first_star(first_ids: list[int], second_ids: list[int]) -> int:
    """Does the first task."""

    return calculate_distance(sorted(first_ids), sorted(second_ids))


def get_second_star(first_ids: list[int], second_ids: list[int]) -> int:
    """Does the second task."""

    return sum([second_ids.count(first_id) * first_id
                for first_id in first_ids])


if __name__ == "__main__":

    input_data = get_input_data(1, test=False)

    ids_1, ids_2 = format_data(input_data)

    print(get_first_star(ids_1, ids_2))
    print(get_second_star(ids_1, ids_2))
