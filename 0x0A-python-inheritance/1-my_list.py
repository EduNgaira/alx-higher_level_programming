#!/usr/bin/python3
"""MyList class container"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """object initialization"""
        super().__init__()

    def print_sorted(self):
        """sorted list printout"""
        print(sorted(self))
