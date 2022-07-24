"""Module with an implementation of a jukugo word node."""
from graph.node import Node
from kanji.word import Word


class JukugoNode(Node):
    """Class representing a jukugo word node."""

    def unique_id(self) -> str:
        return ','.join(self.value.get_all_representations())

    def __init__(self, value: Word):
        super().__init__()
        self.value = value
