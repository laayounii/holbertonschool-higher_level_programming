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
            return {att: self.__dict__[att] for
                    att in attrs if hasattr(self, att)}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
