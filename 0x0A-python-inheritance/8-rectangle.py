#!/usr/bin/python3

""" 
Class inherits from BaseGeometry 
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle representation"""

    def __init__(self, width, height):
        """
        Initializing function
            Args:
                width: rectangle breadth
                height: rectangle length
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Rectangular area"""
        return self.__width * self.__height

    def __str__(self):
        """informal rectangle string representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
