#!/usr/bin/python3
"""
Module 1-rectangle
Defines a class Rectangle with private
instance attributes width and height
and property and setter for both
"""


class Rectangle:
    """
    Defines a rectangle with private
    instance attributes width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.
        Args:
            width (int): The width.
            height (int): The height .
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        Args:
            value (int): The value to set the width to.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        Args:
            value (int): The value to set the height to.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
