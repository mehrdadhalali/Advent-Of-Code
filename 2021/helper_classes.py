"""This script is for useful classes that are handy in different scripts."""


class Node:
    """A node in a graph."""

    def __init__(self, name: str):

        self.name = name
        self.neighbours = set()


class LinkedList:
    """A linked list."""

    def __init__(self, value):

        self.value = value
        self.next = None

    def __repr__(self) -> str:

        if self.next is not None:

            return str(self.value) + str(self.next)

        return str(self.value)
