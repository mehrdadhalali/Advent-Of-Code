"""Day 10"""
from helper_functions import get_input_data

CLOSED_TO_OPEN = {
    "]": "[",
    "}": "{",
    ")": "(",
    ">": "<"
}

OPEN_TO_CLOSED = {op: cl
                  for (cl, op) in CLOSED_TO_OPEN.items()}


BRACKET_POINTS_INCOMPLETE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

BRACKET_POINTS_CORRUPT = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


def find_problem(brackets: str) -> dict:
    """Determines if a string of brackets is corrupted or incomplete."""

    open_brackets = []
    for char in brackets:
        if char in ["[", "{", "<", "("]:
            open_brackets.append(char)
        elif CLOSED_TO_OPEN[char] != open_brackets.pop(-1):
            return {"status": "corrupt",
                    "corrupt_character": char}

    if len(open_brackets) > 0:
        return {"status": "incomplete",
                "open_brackets": "".join(open_brackets)}

    return {"status": "correct"}


def find_closing_sequence(open_brackets: str) -> list[str]:
    """Given a list of open brackets, finds their unique closing string."""

    closing_brackets = [OPEN_TO_CLOSED[bracket]
                        for bracket in open_brackets]
    return "".join(list(reversed(closing_brackets)))


def calculate_autocomplete_score(closing_brackets: str) -> int:

    auto_score = 0
    for bracket in closing_brackets:
        auto_score *= 5
        auto_score += BRACKET_POINTS_INCOMPLETE[bracket]

    return auto_score


def get_first_star(data: list[str]) -> int:
    """Does the first task."""

    wrongness = 0
    for line in input_data:
        problem = find_problem(line)
        if problem["status"] == "corrupt":
            wrongness += BRACKET_POINTS_CORRUPT[problem["corrupt_character"]]

    return wrongness


def get_second_star(data: list[str]) -> int:
    """Does the second task."""

    autocomplete_scores = []
    for line in input_data:
        problem = find_problem(line)
        if problem["status"] == "incomplete":
            autocomplete_scores.append(calculate_autocomplete_score(
                find_closing_sequence(problem["open_brackets"])))

    autocomplete_scores.sort()
    return autocomplete_scores[(len(autocomplete_scores)-1)//2]


if __name__ == "__main__":

    input_data = get_input_data(10, test=False)

    print(get_first_star(input_data))
    print(get_second_star(input_data))
