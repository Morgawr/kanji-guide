"""Module with an implementation of a kunyomi/kana word node."""
from graph.node import Node
from kanji.word import WordGroup


class KanaNode(Node):
    """Class representing a kana-only word node."""

    def unique_id(self) -> str:
        return ','.join(
            [','.join(word.get_all_representations())
             for word in self.value.words])

    def __init__(self, value: WordGroup):
        super().__init__()
        self.value = value
