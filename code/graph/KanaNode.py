from graph.Node import Node
from kanji.Word import Word


class KanaNode(Node):

    def UniqueID(self) -> str:
        return ','.join(self.value.GetAllRepresentations())

    # TODO(morg): Handle kana nodes with multiple kana words like transitive vs
    # intransitive pairs being considered a single word group.
    def __init__(self, value: Word):
        super().__init__()
        self.value = value
