#!/usr/bin/python3
"""Module for the Square class."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (float or int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.

        """
        self.size = size

    @property
    def size(self):
        """Retrieve the value of the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the size attribute.

        Args:
            value (float or int): The new value for the size attribute.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.

        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if the area of one square is less than the area of another."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if the area of one square is less than or equal to the area of another."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if the area of one square is greater than the area of another."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if the area of one square is greater than or equal to the area of another."""
        return self.area() >= other.area()
