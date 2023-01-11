#!/usr/bin/python3


class Student:
    """

    Defines A student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes Object
            Args =  attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns  ddictionary representation of object

        """

        return (self.__dict__)
