#!/usr/bin/python3
# 1-rectangle.py
"""Rectangle class definition."""


class Rectangle:
    """Represents rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Arguments:
            width (int): New rectangle width.
            height (int): New rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width should be an integer")
        if value < 0:
            raise ValueError("width is >= 0")
        self.__width = value

    @property
    def height(self):
        """Set rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height should be an integer")
        if value < 0:
            raise ValueError("height should be >= 0")
        self.__height = value
