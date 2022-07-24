"""Module with an implementation of a kunyomi/kana word node."""
from graph.node import Node
from kanji.word import Word


class KanaNode(Node):
    """Class representing a kana-only word node."""

    def unique_id(self) -> str:
        return ','.join(self.value.get_all_representations())

    # TODO(morg): Handle kana nodes with multiple kana words like transitive vs
    # intransitive pairs being considered a single word group.
    def __init__(self, value: Word):
        super().__init__()
        self.value = value
