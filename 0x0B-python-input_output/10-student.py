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

    def to_json(self, attrs=None):
        """
        Args
            attrs -> list of attributes

        Returns  ddictionary representation of object
        """
        if attrs is None:
            return (self.__dict__)

        my_dict = []
        if isinstance(attrs, list):
            for e in attrs:
                if not isinstance(e, str):
                    return (self.__dict__)
            for k, v in self.__dict__.items():
                t = (k, v)
                for e in attrs:
                    if e == k:
                        my_dict.append(t)
            return dict(my_dict)
