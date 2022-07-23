from __future__ import annotations


class Node:

    def __init__(self):
        self._neighbors = set()
        self._visited = False

    def UniqueID(self) -> str:
        """Returns a string unique identifier representing this node entry."""
        raise NotImplementedError

    def __eq__(self, other):
        return str(self) == str(other)

    def __str__(self):
        return self.UniqueID()

    def __hash__(self):
        return hash(self.UniqueID())

    def IsNeighbor(self, node: Node) -> bool:
        """Checks whether the other node is a neighbor of us or not."""
        return node in self._neighbors

    def AddNeighbor(self, node: Node) -> None:
        """Bidirectinally becomes neighbor with the other node.

        This method recursively calls itself on the other node to check whether
        or not the current self node exists in the other set of neighbors.
        It can potentially run forever if it enters a broken loop so make sure
        the UniqueID() and IsNeighbor() methods work as expected or we're going
        to be in for a rough debugging time.
        """
        if self == node:
            return
        if not self.IsNeighbor(node):
            self._neighbors.add(node)
            node.AddNeighbor(self)
        elif not node.IsNeighbor(self):
            node.AddNeighbor(self)

    def RemoveNeighbor(self, node: Node):
        """Bidirectionally severs the neighbor relationship with the other node.

        Same as AddNeighbor, we want to make sure there's no weird recursive
        action happening.
        """
        if self == node:
            return
        if self.IsNeighbor(node):
            self._neighbors.remove(node)
            node.RemoveNeighbor(self)
        elif node.IsNeighbor(self):
            node.RemoveNeighbor(self)

    def MarkVisited(self):
        self._visited = True

    def HasBeenVisited(self):
        return self._visited
