"""Module containing the implementation of a kanji graph data structure

A graph can be composed of multiple nodes, each node can be one of the
following:
    - A kunyomi/kana word (e.g.: たべる, すき, いぬ, etc)
    - A jukugo word (e.g.: 事実, 主人, 原因, etc)
    - A kanji (e.g.: 木, 食, etc)

Each node is connected to nearby nodes based on its structure and common kanji
being shared between them.
For example:
    - The kana word まなぶ can be represented as 学ぶ, so it will be connected
      to the kanji node 学.
    - The jukugo 学校 also uses the kanji 学 so it will be connected to it, as
      well as the kanji 校.
    - The kanji node 学 will have at least two connections (to 学校 and 学ぶ)
    - 学校 will also be connected to the kanji node 校
    - etc etc

Kunyomi entries do not have a frequency value, however both kanji **and** jukugo
nodes will have a frequency value that is used to determine the "weight" of each
node compared to its neighbor. The graph walking algorithm will use a heuristic
approach based on these values (+ some manual finetuning and list of priority
rules that is still TBD).
"""

from corpus.corpus import Corpus
from kanji.word import Word
from graph.node import Node
from graph.kana_node import KanaNode
from graph.jukugo_node import JukugoNode
from graph.kanji_node import KanjiNode

class Graph:
    """Class representing a corpus-based kanji mapping graph data structure."""

    # TODO(morg): complete this class once we have proper corpus loading
    def __init__(self, corpus: Corpus):
        self.corpus = corpus
