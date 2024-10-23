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


def get_element_occurrences(template: LinkedList) -> list[tuple]:
    """Returns a list of tuples showing how many times an element is in the template."""

    occurrences = {}

    while template is not None:

        occurrences[template.value] = occurrences.get(template.value, 0) + 1
        template = template.next

    return occurrences.items()


def get_first_star(template: LinkedList, rules: dict) -> int:
    """Does the first task."""

    for _ in range(0, 10):
        template = insert_elements(template, rules)

    occurrences = get_element_occurrences(template)

    occurrences = sorted(occurrences, key=lambda x: x[1])

    return occurrences[-1][1] - occurrences[0][1]


if __name__ == "__main__":

    input_data = get_input_data(14, test=False)
    polymer_template, insertion_rules = format_data(input_data)

    print(get_first_star(polymer_template, insertion_rules))
