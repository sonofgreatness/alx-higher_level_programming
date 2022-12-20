#!/usr/bin/python3
class Square:
    __size = None

    def __init__(self, size=0):
        """
        Args:
           size(int) , size of square
        Raises:
            TypeError  if size in not int
            ValueError if size < 0
        """

        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
