#!/usr/bin/python3
"""
Defines rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Rectangle initialization

        Args:
            width (int): New rectangle width.
            height (int): New Rectangle height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
