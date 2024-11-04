"""Day 14"""

from helper_functions import get_input_data
from helper_classes import LinkedList


def format_template(template_list: list[str]) -> LinkedList:
    """Formats the template into a linked list."""

    elements = [LinkedList(item)
                for item in template_list]
    for i in range(0, len(elements)-1):
        elements[i].next = elements[i+1]

    return elements[0]


def format_rules(rules_str: list[str]) -> dict:
    """Formats the rules into a dictionary."""

    rules = {}
    for rule in rules_str:
        left, right = tuple(rule.split(" -> "))
        rules[left] = right

    return rules


def format_data(data: list[str]) -> dict:
    """Formats the data properly."""

    template = list(data[0])
    rules_str = data[2:]

    return format_template(template), format_rules(rules_str)


def insert_elements(template: LinkedList, rules: dict) -> LinkedList:
    """Performs the pair insertion process once."""

    first_element = template

    while template.next is not None:

        new_element_val = rules[template.value + template.next.value]
        new_element = LinkedList(new_element_val)
        new_element.next = template.next
        template.next = new_element
        template = template.next.next

    return first_element


def execute_steps(template: LinkedList, rules: dict, steps: int) -> LinkedList:
    """Performs the pair insertion multiple times."""

    for _ in range(0, steps):
        template = insert_elements(template, rules)


def get_element_occurrences(template: LinkedList) -> list[tuple]:
    """Returns a list of tuples showing how many times an element is in the template."""

    occurrences = {}

    while template is not None:

        occurrences[template.value] = occurrences.get(template.value, 0) + 1
        template = template.next

    return occurrences


def return_occurrences_after_steps(template: LinkedList, rules: dict,
                                   step_count: int) -> dict:
    """Given a base template, the rules, and a number of steps,
        returns the occurrences of every letter after that number of steps."""

    execute_steps(template, rules, step_count)

    occurrences = get_element_occurrences(template)

    return occurrences


def get_first_star(template: LinkedList, rules: dict) -> int:
    """Does the first task."""

    occurrences = return_occurrences_after_steps(template, rules, 10)

    return occurrences[-1][1] - occurrences[0][1]


def get_unique_letters(rules: dict) -> list[str]:
    """Returns all of the unique letters in the ruleset."""

    return list(set([letter
                for key in rules.keys()
                for letter in list(key)]))


def create_cached_occurrences(pairs: list[LinkedList], rules: dict, step_count: int) -> dict:
    """Given a list of pair, returns an object that maps the pair
        to the occurrences after some amount of steps.
        The occurrences exclude the original parents."""

    total = len(pairs)
    cached_occurrences = {}

    for i in range(0, len(pairs)):
        key = str(pairs[i])
        occurrences = return_occurrences_after_steps(
            pairs[i], rules, step_count)

        p1, p2 = tuple(key)
        occurrences[p1] = occurrences[p1] - 1
        occurrences[p2] = occurrences[p2] - 1

        cached_occurrences[key] = occurrences
        if i % 5 == 4 and i > 0:
            print(f"Caching: {i+1}/{total}")

    return cached_occurrences


def update_occurrences(occ_1: dict, occ_2: dict) -> dict:
    """Updates the first occurrence with the second one."""

    for key in occ_2.keys():
        occ_1[key] = occ_1.get(key, 0) + occ_2[key]

    return occ_1


def get_second_star(template: LinkedList, rules: dict) -> int:
    """Does the second task."""

    unique_letters = get_unique_letters(rules)
    pairs = [format_template(list(char1 + char2)) for char1 in unique_letters
             for char2 in unique_letters]

    cached_occurrences = create_cached_occurrences(pairs, rules, 20)

    occurrences_main = return_occurrences_after_steps(template, insertion_rules,
                                                      20)

    template_str = str(template)
    for i in range(0, len(template_str) - 1):

        to_add = cached_occurrences[template_str[i]+template_str[i+1]]
        update_occurrences(occurrences_main, to_add)

    occurrences_list = sorted(occurrences_main.items(), key=lambda x: x[1])
    return occurrences_list[-1][1] - occurrences_list[0][1]


if __name__ == "__main__":

    input_data = get_input_data(14, test=False)
    polymer_template, insertion_rules = format_data(input_data)

    print(get_first_star(polymer_template, insertion_rules))
    print(get_second_star(polymer_template, insertion_rules))

    # TODO: Task 2 takes a few minutes, make it faster.
