"""Day 5"""

from helper_functions import get_input_data


def format_data(lines: list[str]) -> tuple:
    """Turns the data into a tuple, of ordering rules and updates."""

    breaker = lines.index("")
    return (lines[0: breaker], lines[breaker + 1:])


def format_rules(rules_str: list) -> dict:
    """Turns the rules into a dictionary in the form:
        {n: [anything that must come before n]}."""

    befores = {}
    for rule in rules_str:
        before, after = map(int, tuple(rule.split("|")))
        befores_list = befores.get(after, [])
        befores_list.append(before)
        befores[after] = befores_list

    return befores


def format_updates(updates_str: list[str]) -> list[list[int]]:
    """Turns the updates into a list of list of ints."""

    return [list(map(int, update.split(",")))
            for update in updates_str]


def is_it_valid(update: list[int], rules: dict) -> bool:
    """A recursive function that tells us if the ordering of an update is valid.
        The method is "guilty until proven innocent":
        Return True, only if no element has a successor that is in its before list. """

    if len(update) == 1:
        return True

    if any(before_element in update[1:]
           for before_element in rules.get(update[0], [])):
        return False

    return is_it_valid(update[1:], rules)


def get_first_star(rules: dict, updates: list[list]) -> int:
    """Does the first task."""

    valid_updates = [update for update in updates
                     if is_it_valid(update, rules)]

    return sum([update[(len(update) - 1)//2]
               for update in valid_updates])


def fix_invalid_update(update: list[int], rules: dict):
    """Sort an invalid update so that it's valid now.
        For each element, swap its position with the last element in front of it
        that shouldn't be there. If no swaps are needed, move forward.
        If there is a swap, stay and repeat until no swaps occur."""

    for i in range(0, len(update) - 1):

        # The indices of all "bad" elements in front of element number i
        invalid_successors = [j for j in range(i+1, len(update))
                              if update[j] in rules.get(update[i], [])]

        while len(invalid_successors) > 0:

            # Take the highest index
            highest_bad_index = invalid_successors[-1]

            # Swap its element with element i
            to_replace = update[highest_bad_index]
            update[highest_bad_index] = update[i]
            update[i] = to_replace

            # re-evaluate the bad successors
            invalid_successors = [j for j in range(i+1, len(update))
                                  if update[j] in rules.get(update[i], [])]

    return update


if __name__ == "__main__":

    input_data = get_input_data(5, False)

    ordering_rules, print_updates = format_data(input_data)

    ordering_rules = format_rules(ordering_rules)
    print_updates = format_updates(print_updates)

    invalid_updates = [update for update in print_updates
                       if not is_it_valid(update, ordering_rules)]

    fixed_updates = [fix_invalid_update(invalid_update, ordering_rules)
                     for invalid_update in invalid_updates]

    print(sum([update[(len(update) - 1)//2]
               for update in fixed_updates]))
