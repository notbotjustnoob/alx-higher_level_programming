#!/usr/bin/python3
"""Module for the MagicClass class."""

import math


class MagicClass:
    """A class that replicates the behavior of the provided Python bytecode."""

    def __init__(self, radius=0):
        """Initialize a MagicClass instance.

        Args:
            radius (float or int, optional): The radius of the circle (default is 0).

        Raises:
            TypeError: If radius is not a number (float or integer).

        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = float(radius)

    def area(self):
        """Calculate and return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius


if __name__ == "__main__":
    mc = MagicClass(5)
    print(mc.area())
    print(mc.circumference())
