"""Module containing the basic abstract node structure of a word graph."""
from __future__ import annotations


class Node:
    """Abstract implementation of a node."""

    def __init__(self):
        self._neighbors = set()
        self._visited = False

    def unique_id(self) -> str:
        """Returns a string unique identifier representing this node entry."""
        raise NotImplementedError

    def __eq__(self, other):
        return str(self) == str(other)

    def __str__(self):
        return self.unique_id()

    def __hash__(self):
        return hash(self.unique_id())

    def is_neighbor(self, node: Node) -> bool:
        """Checks whether the other node is a neighbor of us or not.

        Args:
            node: the node to check
        """
        return node in self._neighbors

    def add_neighbor(self, node: Node) -> None:
        """Bidirectinally becomes neighbor with the other node.

        This method recursively calls itself on the other node to check whether
        or not the current self node exists in the other set of neighbors.
        It can potentially run forever if it enters a broken loop so make sure
        the unique_id() and is_neighbor() methods work as expected or we're
        going to be in for a rough debugging time.

        Args:
            node: the neighbor node to add
        """
        if self == node:
            return
        if not self.is_neighbor(node):
            self._neighbors.add(node)
            node.add_neighbor(self)
        elif not node.is_neighbor(self):
            node.add_neighbor(self)

    def remove_neighbor(self, node: Node):
        """Bidirectionally severs the neighbor relationship with the other node.

        Same as add_neighbor, we want to make sure there's no weird recursive
        action happening.

        Args:
            node: the neighbor node to remove
        """
        if self == node:
            return
        if self.is_neighbor(node):
            self._neighbors.remove(node)
            node.remove_neighbor(self)
        elif node.is_neighbor(self):
            node.remove_neighbor(self)

    def mark_visited(self):
        """Marks the node as visited."""
        self._visited = True

    def is_visited(self) -> bool:
        """Checks if the node has been visited."""
        return self._visited
