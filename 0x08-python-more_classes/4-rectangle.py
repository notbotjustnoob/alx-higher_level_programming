#!/usr/bin/python3
"""
Defines a class Rectangle with
private instance attributes width
and height, property and setter
for both, methods to calculate
area and perimeter, string
representation method, and a
method to return an official string
representation that can recreate
a new instance with eval().
"""


class Rectangle:
    """
    Defines a rectangle with private
    instance attributes width and height,
    and methods to calculate area and perimeter,
    provide string representations,
    and an official string representation
    to recreate a new instance.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
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

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        If width or height is equal to 0, perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle with '#'.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rectangle_str)

    def __repr__(self):
        """
        Returns an official string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"
