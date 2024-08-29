"""Day 3"""

from read_from_file import get_input_data


def sum_position_at(readings: list[list], position: int) -> int:
    """Sums up all of the readings at index `position`"""

    return sum([int(reading[position]) for reading in readings])


def get_majority_readings(readings: list[list], position: int) -> list[list]:
    """Returns the list of readings with a majority on a given position."""

    number_of_readings = len(readings)
    if number_of_readings % 2 == 0:
        half = number_of_readings // 2
    else:
        half = number_of_readings // 2 + 1

    total = sum_position_at(readings, position)

    majority = int(total >= half)

    return [reading for reading in readings if int(reading[position]) == majority]


def get_the_majority_string(readings: list[list]) -> list:
    """Returns"""


def bin_to_int(bits: list[int]) -> int:
    """Turns a bitstring in list form into the corresponding integer."""

    total = 0
    for i in range(0, len(bits)):
        total += bits[i] * 2**(len(bits)-i-1)

    return total


def get_first_star(readings: list[list]) -> int:
    """Does the first task."""

    number_of_inputs = len(readings)
    length_of_one_reading = len(readings[0]) - 1

    # Calculate the sum of all readings added pointwise
    input_totals = [sum_position_at(readings, i)
                    for i in range(0, length_of_one_reading)]

    # At every position, if the sum is less than half of the number of readings, then
    # the majority must be 0's, otherwise it's 1's
    gamma_reading = [int(entry >= number_of_inputs // 2)
                     for entry in input_totals]

    gamma_reading_int = bin_to_int(gamma_reading)

    # epsilon == map NOT gamma, so the final answer is a function of gamma only
    return gamma_reading_int * ((2**length_of_one_reading-1)-gamma_reading_int)


def get_second_star(readings: list[list]) -> int:
    """Does the second task."""

    length_of_one_reading = len(readings[0]) - 1

    for i in range(0, length_of_one_reading):
        readings = get_majority_readings(readings, i)
        print(["".join(reading) for reading in readings])
        if len(readings) == 1:
            break
    return "".join(readings[0])


if __name__ == "__main__":
    input_readings = [list(line) for line in get_input_data(3)]

    # print(get_first_star(input_readings))
    print(get_second_star(input_readings))
