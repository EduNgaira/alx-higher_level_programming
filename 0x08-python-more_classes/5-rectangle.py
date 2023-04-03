#!/usr/bin/python3
# 5-rectangle.py
"""Rectangle"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Rectangle.Initialization.
        Arguments:
            width (int): New rectangle width.
            height (int): New rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set rectangle width."""
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        """Set rectangle height."""
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value

    def area(self):
        """Return rectangle area"""
        return (self.width * self.height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """Return rectangle representation.
        Represents the rectangle with the # character.
        """
        if self.width == 0 or self.height == 0:
            return ("")

        rect = []
        for i in range(self.height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return rectangle representation"""
        rect = "Rectangle(" + str(self.width)
        rect += ", " + str(self.height) + ")"
        return (rect)

    def __del__(self):
        """Message for every deletion of rectangle."""
        print("Bye rectangle...")
