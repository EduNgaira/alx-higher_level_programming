#!/usr/bin/python3
"""
Defines class BaseGeometry
"""


class BaseGeometry:
    """Base geometry."""

    def area(self):
        """if not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer parameter.

        Args:
            name (str): Parameter name
            value (int): Parameter to validate.
        Raises:
            TypeError: If non-integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
