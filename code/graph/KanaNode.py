from Node import Node

class KanaNode(Node):

    def UniqueID(self) -> str:
        #TODO(morg): Implement the kana data layer
        return "Placeholder" + str(self.value)

    def __init__(self, value: int):
        super().__init__()
        self.value = value
