"""Module with an implementation of a jukugo word node."""
from graph.node import Node
from kanji.word import Word
from corpus.corpus import Corpus


class JukugoNode(Node):
    """Class representing a jukugo word node."""

    def unique_id(self) -> str:
        return ','.join(self.value.get_all_representations())

    def __init__(self, value: Word, corpus: Corpus):
        super().__init__()
        self.value = value
        self.frequency = corpus.get_freq(str(self.value.default_representation))
