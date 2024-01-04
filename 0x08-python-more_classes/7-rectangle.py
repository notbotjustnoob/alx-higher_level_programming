#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """
    Rectangle: Manages width, height, print_symbol.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initialize width, height. """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieve width. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width. Check validity. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve height. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height. Check validity. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculate area. """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculate perimeter. """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ String representation using print_symbol. """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        rectangle_str = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(rectangle_str)

    def __repr__(self):
        """ Official string representation. """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Destructor. Decrements count. """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
