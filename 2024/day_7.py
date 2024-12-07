"""Day 7"""

from helper_functions import get_input_data


def format_data(lines: list) -> list[list]:
    """Returns a list of lists, each inner list an equation.
        The first number in the inner list is the input number,
        others are the calibrating ones."""

    formatted_lines = []
    for line in lines:

        in_out = line.split(":")
        first_number = int(in_out[0])
        other_numbers = list(map(int, in_out[1][1:].split(" ")))

        formatted_lines.append([first_number] + other_numbers)

    return formatted_lines


def create_all_bitstrings(length: int) -> list[list[bool]]:
    """Generates all bitstrings of length n."""

    if length == 1:
        return ["0", "1"]

    return (["0" + b for b in create_all_bitstrings(length - 1)]
            + ["1" + b for b in create_all_bitstrings(length - 1)])


def create_all_tritstrings(length: int) -> list[list[bool]]:
    """Generates all bitstrings of length n."""

    if length == 1:
        return ["0", "1", "2"]

    return (["0" + b for b in create_all_tritstrings(length - 1)]
            + ["1" + b for b in create_all_tritstrings(length - 1)]
            + ["2" + b for b in create_all_tritstrings(length - 1)])


def evaluate_expression(numbers: list[int], tritstring: str) -> int:
    """Given a list of numbers, and a specific tritstring for their operations,
        returns the result of the expression.
        (0 = add, 1 = times, 2 = conc)"""

    if len(tritstring) != len(numbers) - 1:
        raise ValueError("The sizes don't match!")

    total = numbers[0]
    for i in range(0, len(tritstring)):

        if tritstring[i] == "0":
            total += numbers[i+1]
        elif tritstring[i] == "1":
            total *= numbers[i+1]
        else:
            total = int(str(total) + str(numbers[i+1]))

    return total


def solve_equation(all_numbers: list[int], strings: list[str],
                   three_ops: bool = False) -> bool:
    """Does this equation have a solution?"""

    test_value = all_numbers[0]
    other_numbers = all_numbers[1:]
    operation_count = len(other_numbers) - 1

    if not three_ops:
        relevant_strings = [string[:operation_count] for string in
                            strings[:2**(operation_count)]]
    else:
        relevant_strings = [string[:operation_count] for string in
                            strings[:3**(operation_count)]]

    for string in relevant_strings:
        if test_value == evaluate_expression(other_numbers, string):
            return True

    return False


def get_first_star(eqs: list) -> int:
    """Does the first task."""

    max_operator_length = max([len(equation) - 2
                               for equation in eqs])

    all_bitstrings = [bitstring[::-1] for bitstring in
                      create_all_bitstrings(max_operator_length)]

    return sum([eq[0] for eq in eqs
                if solve_equation(eq, all_bitstrings)])


def get_second_star(eqs: list) -> int:
    """Does the second task."""

    max_operator_length = max([len(equation) - 2
                               for equation in eqs])

    all_tritstrings = [tritstring[::-1] for tritstring in
                       create_all_tritstrings(max_operator_length)]

    return sum([eq[0] for eq in eqs
                if solve_equation(eq, all_tritstrings, True)])


if __name__ == "__main__":

    input_data = get_input_data(7, test=False)

    equations = format_data(input_data)

    print(get_first_star(equations))
    print(get_second_star(equations))
