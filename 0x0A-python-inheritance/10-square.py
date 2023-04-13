#!/usr/bin/python3
"""
Rectangle subclass Square defined
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """Square initialization.

        Args:
            size (int): New square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
