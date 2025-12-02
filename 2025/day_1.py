"""Day 1"""

from helper_functions import get_input_data

def format_data(lines: list) -> list[tuple]:
    """Return the instruction in a list of tuples."""

    return [(line[0], int(line[1:])) for line in lines]

def move_dial(current_number: int, instruction: str) -> int:
    """Moves the dial once according to the instruction."""

    if instruction[0] == "R":
        return current_number + instruction[1]
    return current_number - instruction[1]

def calculate_zero_points(old_number: int, new_number: int) -> int:
    """How many times did we point to zero in this one instruction?"""

    distance = abs((old_number // 100) - (new_number // 100))

    if old_number % 100 == 0 and new_number < old_number and distance > 0:
        distance -= 1
    
    if new_number % 100 == 0 and new_number < old_number:
        distance += 1
    
    return distance
            

def simulate_dial(instructions: list) -> tuple:
    """Move the dial as per the instructions."""

    dial_number = 50
    zero_dial_numbers = 0
    zero_point_count = 0

    for ins in instructions:
        new_dial_number = move_dial(dial_number, ins)
        if new_dial_number % 100 == 0:
            zero_dial_numbers += 1
        
        zero_point_count += calculate_zero_points(dial_number, new_dial_number)
        dial_number = new_dial_number
    
    return zero_dial_numbers, zero_point_count

if __name__ == "__main__":
    
    instructions = format_data(get_input_data(1, test=False))
    print(simulate_dial(instructions))

