#!/usr/bin/python3

class Square:
    __size = None
    __position = None 
    def __init__(self, size=0, position = (0,0)):
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
        

        if type(position) == tuple: 
            if (position[0] >= 0 and position[1] >= 0): 
                self.__position = position 
            else: 
                raise TypeError("position must be a tuple of 2 positive integer")
        else: 
            raise TypeError("position must be a tuple of 2 positive integers")

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
        Raises 
            ValueError if value > 0 
            TypeError if value is not of type int 
        """
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")


    @property 
    def position(self):
        """
        getter function for the attribute :position 

        """
        

        return self.__position

    @position.setter
    def position(self, value):
        """
        setter function for the attribute position
        
        Args 
           value (tuple) -> parameter to set to  position 
        """
        
        if type(value) == tuple: 
             if (value[0] >= 0 and value[1] >= 0): 
                 self.__position = value
             else: 
                 raise TypeError("position must be a tuple of 2 positive integers")
        else: 
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):

        """
        prints  square using hash character (#)
        """
        if (self.__size == 0):
            print()
        for i in range(self.__size + self.__position[1]):
                for k in range(self.__position[0]):
                    if (self.__position[1] > 0):
                        print("_", end="")
                    else: 
                        print(" ",end="")
                for j in range(self.__size):
                        print("#", end="")
                print()
