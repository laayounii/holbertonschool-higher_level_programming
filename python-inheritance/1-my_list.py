#!/usr/bin/python3
"""
    A subclass of list that provides a method to
    print a sorted version of itself.
    """


class MyList(list):
    """
    A subclass of list that provides a method to
    print a sorted version of itself.

    Attributes:
        new_list (list): An instance of a list.
    """

    def print_sorted(self):
        """
        Prints the sorted version of the list.
        """
        print(sorted(self))
