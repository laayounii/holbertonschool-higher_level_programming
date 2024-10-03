#!/usr/bin/python3
"""class Student"""


class Student:
    """Initialize Student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Converts the Student object to a JSON-compatible dictionary."""
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    my_dict.update({att: self.__dict__[att]})
            return my_dict
