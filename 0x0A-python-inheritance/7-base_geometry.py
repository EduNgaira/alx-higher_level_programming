#!/usr/bin/python3
"""
Function 6-base_geometry.py container
"""


class BaseGeometry:
    """Public instance methods area and integer_validator class"""
    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Shows value is greater than 0 and an integer"""
        if type(value) is not int:
            raise TypeError("{:s} is an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} is greater than 0".format(name))
