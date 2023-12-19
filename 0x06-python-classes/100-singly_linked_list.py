#!/usr/bin/python3
"""Module for the SinglyLinkedList class."""


class Node:
    """A class that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a Node instance.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The next node in the linked list
                (default is None).

        Raises:
            TypeError: If data is not an integer or if next_node is not a Node
                object.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the value of the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of the data attribute.

        Args:
            value (int): The new value for the data attribute.

        Raises:
            TypeError: If value is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node attribute.

        Args:
            value (Node or None): The new value for the next_node attribute.
                It can be a Node object or None.

        Raises:
            TypeError: If value is not a Node object or None.

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """Initialize a SinglyLinkedList instance with an empty head."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to be stored in the new Node.

        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list."""
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
