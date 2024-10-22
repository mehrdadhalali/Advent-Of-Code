"""This script is for useful classes that are handy in different scripts."""


class Node:
    """A node in a graph."""

    def __init__(self, name: str):

        self.name = name
        self.neighbours = set()
