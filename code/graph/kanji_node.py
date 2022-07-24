"""Module with an implementation of a kanji node."""
from graph.node import Node


class KanjiNode(Node):
    """Class representing a kanji node."""

    def unique_id(self) -> str:
        return self.value

    # TODO(morg): Make value a proper kanji object
    def __init__(self, value: str, corpus: Corpus):
        super().__init__()
        self.value = value
        self.frequency = corpus.get_freq(value)
