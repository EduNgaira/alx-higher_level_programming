#!/usr/bin/python3
"""
Defines a class MyInt that inherits from int.
"""


class MyInt(int):
    """Inverts operators == and !=."""

    def __eq__(self, value):
        """Override == with != behavio operator."""
        return self.real != value

    def __ne__(self, value):
        """Override != with == behavior operator."""
        return self.real == value
