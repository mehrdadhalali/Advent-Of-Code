"""Day 12"""
from helper_functions import get_input_data
from helper_classes import Node


class Cave(Node):
    """A cave is like a node in a graph, but it has a size."""

    def __init__(self, name):

        super().__init__(name)
        self.is_big = self.name.isupper()

    def __repr__(self) -> str:
        return self.name

    def copy(self):
        """Creates a deep copy of the cave."""

        duplicate = Cave(self.name)
        duplicate.neighbours = self.neighbours.copy()

        return duplicate


def format_data(data: list[str]) -> list[list[str]]:
    """Separates the cave names."""

    return [line.split("-")
            for line in data]


def create_caves(formatted_data: list[list[str]]) -> list[Cave]:
    """Returns a list of all the caves."""

    all_cave_names = {cave_name for pair in formatted_data
                      for cave_name in pair}

    return [Cave(cave_name)
            for cave_name in all_cave_names]


def find_cave_by_name(cave_name: str, caves: list[Cave]) -> Cave:
    """Returns a cave by its name, from a list."""

    return [cave for cave in caves
            if cave.name == cave_name][0]


def connect_caves(caves: list[Cave], name_pairs: list[list[str]]):
    """Connects the caves together."""

    for name_pair in name_pairs:
        cave_1 = find_cave_by_name(name_pair[0], caves)
        cave_2 = find_cave_by_name(name_pair[1], caves)

        cave_1.neighbours.add(cave_2)
        cave_2.neighbours.add(cave_1)


def find_paths(path: list[Cave], current_cave: Cave) -> list[list[str]]:
    """Find the number of paths from this cave to the end."""

    path_so_far = path.copy()

    if current_cave.name == "end":
        return [path + [current_cave]]

    path_so_far.append(current_cave)

    explorable = [neighbour
                  for neighbour in current_cave.neighbours
                  if neighbour.is_big
                  or neighbour not in path_so_far]

    return ([path
             for cave in explorable
             for path in find_paths(path_so_far, cave)])


if __name__ == "__main__":

    input_data = get_input_data(12, test=False)
    paired_data = format_data(input_data)

    caves = create_caves(paired_data)

    connect_caves(caves, paired_data)

    print(len(find_paths([], find_cave_by_name("start", caves))))
