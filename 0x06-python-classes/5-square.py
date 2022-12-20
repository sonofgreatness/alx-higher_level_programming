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

    @property
    def size(self):
        """
        getter function for size attribute
        Returns
            size field
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """
        setter function for size attribute
        Args
            value (int)  -> parameter that to set size to
        """
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """
        prints  square using hash character (#)
        """
        if (self.__size == 0):
            print()
        for i in range(self.__size):
                for j in range(self.__size):
                        print("#", end="")
                print()
