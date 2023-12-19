#!/usr/bin/python3
"""Module for the Square class."""


class Square:
    """A class that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance.

        Args:
            size (int, optional): The size of the square (default is 0).
            position (tuple of int, optional): The position of the square
                (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or if position is not a tuple of
                two positive integers.
            ValueError: If size is less than 0 or if position contains non-positive
                integers.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the value of the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the size attribute.

        Args:
            value (int): The new value for the size attribute.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the value of the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value of the position attribute.

        Args:
            value (tuple of int): The new value for the position attribute
                (a tuple of two positive integers).

        Raises:
            TypeError: If value is not a tuple of two positive integers.

        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the '#' character, considering the position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
