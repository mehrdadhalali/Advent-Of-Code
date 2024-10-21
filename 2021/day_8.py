"""Day 8"""
from helper_functions import get_input_data

"""Given a wiring, the code of each letter is defined to be te number of times that letter appears in
a string of length 3,4,6 in the input. 
The constant CODE_TO_LETTER indicates the code of each letter, when all the wires are attached correctly."""

CODE_TO_LETTER = {"103": "a",
                  "013": "b",
                  "112": "c",
                  "012": "d",
                  "002": "e",
                  "113": "f",
                  "003": "g"}

LETTERS_TO_DIGIT = {"abcefg": "0",
                    "cf": "1",
                    "acdeg": "2",
                    "acdfg": "3",
                    "bcdf": "4",
                    "abdfg": "5",
                    "abdefg": "6",
                    "acf": "7",
                    "abcdefg": "8",
                    "abcdfg": "9"}


def get_inputs_outputs(line: str) -> tuple[list[str]]:
    """Given a line, returns the inputs and the inputs as a tuple."""

    delimiter_index = line.find("|")

    return (line[:delimiter_index-1].split(" "),
            line[delimiter_index+2:].split(" "))


def calculate_codes(line_inputs: list[str]) -> dict:
    """Given the inputs of a line, returns each letter, along with its code."""

    letter_to_code = {char: "" for char in "abcdefg"}

    for i in [3, 4, 6]:
        for letter in "abcdefg":
            letter_to_code[letter] += str(len([string
                                               for string in line_inputs
                                               if len(string) == i
                                               and letter in string]))

    return letter_to_code


def calculate_wiring(line_inputs: list[str]):
    """Given a line of inputs, return how the wiring was done."""

    letter_to_code = calculate_codes(line_inputs)

    return {letter: CODE_TO_LETTER[letter_to_code[letter]]
            for letter in "abcdefg"}


def decrypt_digit(encrypted_output: str, wiring: dict) -> str:
    """Given a string, and the wiring, calculates the digit that would light up."""

    actual_output = ""

    for letter in encrypted_output:
        actual_output += wiring[letter]

    actual_output = "".join(sorted(actual_output))

    return LETTERS_TO_DIGIT[actual_output]


def calculate_output_number(line_output: list[str], wiring: dict) -> int:
    """Given an output line, calculates the 4 digit code it represents."""

    return int("".join([decrypt_digit(string, wiring)
                        for string in line_output]))


def get_first_star(data: list[str]) -> int:
    """Does the first task."""

    return len([output for input_line in data
                for output in get_inputs_outputs(input_line)[1]
                if len(output) in [2, 3, 4, 7]])


def get_second_star(data: list[str]) -> int:

    total = 0
    for line in data:
        line_input, line_output = get_inputs_outputs(line)

        wiring = calculate_wiring(line_input)
        output_number = calculate_output_number(line_output, wiring)
        total += output_number

    return total


if __name__ == "__main__":

    input_data = get_input_data(8)

    print(get_first_star(input_data))
    print(get_second_star(input_data))
