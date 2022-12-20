#!/usr/bin/python3
class Square:
    __size = None

    def __init__(self, size=0):
        """
        Initializes Square object
        Args
            size (int)   of square size
        Raises
            TypeError - if size is not an integer
            ValueError - if size < 0
        """
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        function to find the area of a square

        Returns
            size*size (int)
        """
        return (self.__size * self.__size)
