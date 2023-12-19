#!/usr/bin/python3
"""Module for the Square class."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
