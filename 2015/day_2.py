
def extract_dimensions(measurement: str) -> tuple[int]:
    """Extracts length, width , height from lengthxwidthxheight."""

    return tuple(map(int, measurement.split("x")))


def calculate_areas(length: int, width: int, height: int) -> list[int]:
    """Returns the three different surface areas of the gift box in square feet."""

    return [length*width, width*height, length*height]


def calculate_paper_needed_per_gift(length: int, width: int, height: int) -> int:
    """Returns the total amount of paper for a single gift given its dimensions."""

    areas = calculate_areas(length, width, height)

    return min(areas) + sum(areas)*2


def calculate_total_paper_needed(measurements: list) -> int:
    """Returns the total amount of paper needed for all gifts."""

    total = 0
    for length, width, height in measurements:

        total += calculate_paper_needed_per_gift(length, width, height)

    return total


if __name__ == "__main__":

    with open("day_2_input.txt", "r", encoding="UTF-8") as f:
        input_measurements = (f.read()).split("\n")

    input_measurements = [extract_dimensions(line)
                          for line in input_measurements]

    print(calculate_total_paper_needed(input_measurements))
