"""Day 3"""

from read_from_file import get_input_data


def calculate_sums(readings: list[list]) -> list[int]:
    """Adds all of the lists pointwise."""

    length_of_one_list = len(readings[0])-1
    totals = [0] * length_of_one_list

    for reading in readings:
        for i in range(0, length_of_one_list):
            totals[i] += int(reading[i])

    return totals


def bin_to_int(bits: list[int]) -> int:
    """Turns a bitstring in list form into the corresponding integer."""

    total = 0
    for i in range(0, len(bits)):
        total += bits[i] * 2**(len(bits)-i-1)

    return total


if __name__ == "__main__":
    input_readings = [list(line) for line in get_input_data(3)]
    number_of_inputs = len(input_readings)
    length_of_one_reading = len(input_readings[0]) - 1

    input_totals = calculate_sums(input_readings)

    gamma_reading = [int(entry > number_of_inputs // 2)
                     for entry in input_totals]

    gamma_reading_int = bin_to_int(gamma_reading)

    print(gamma_reading_int * ((2**length_of_one_reading-1)-gamma_reading_int))
