from graph.Node import Node
from kanji.Word import Word


class JukugoNode(Node):

    def UniqueID(self) -> str:
        return ','.join(self.value.GetAllRepresentations())

    def __init__(self, value: Word):
        super().__init__()
        self.value = value
