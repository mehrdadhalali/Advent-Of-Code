"""Day 3"""

from helper_functions import get_input_data

def format_data(lines: list) -> list[tuple]:
    """Return the data as a list of list of numbers."""

    return [list(map(int,list(line))) for line in lines]

def calculate_max_bank_joltage(bank: list[int], digits: int) -> str:
    """Given a bank, and a digit count, what's the maximum joltage of those number of digits?"""

    highest = max(bank)
    highest_first_pos = bank.index(highest)
    

    if digits == 1:
        return str(highest)

    if len(bank) - highest_first_pos < digits:
        return calculate_max_bank_joltage(bank[:highest_first_pos], digits - len(bank[highest_first_pos:])) + "".join(map(str,bank[highest_first_pos:]))
    
    return str(highest) + calculate_max_bank_joltage(bank[highest_first_pos+1:], digits - 1)


def get_first_star(banks: list[int]) -> int:
    """Does the first task."""
    
    return sum(map(int,[calculate_max_bank_joltage(bank, 2) for bank in banks]))

def get_second_star(banks: list[int]) -> int:
    """Does the second task."""

    return sum(map(int,[calculate_max_bank_joltage(bank, 12) for bank in banks]))

if __name__ == "__main__":
    
    banks = format_data(get_input_data(3, False))

    print(get_first_star(banks))
    print(get_second_star(banks))
