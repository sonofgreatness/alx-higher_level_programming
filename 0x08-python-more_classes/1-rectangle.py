#!/usr/bin/python3
class Rectangle:
    """Defines a rectangle class"""
    def __init__(self, width=0, height=0):
        """method that initializes object
            Args
        width(int) -> width of rectangle
        height(int) -> height of rectangle

        Return
            returns void
        """

        if not isinstance(width, int):
            raise TypeError("width must be integer")
        if width < 0:
            raise ValueError("width must be >=0")
        if not isinstance(height, int):
            raise TypeError("height must be integer")
        if height < 0:
            raise ValueError("height must be >=0")

        self.__width__ = width
        self.__height__ = height

    @property
    def width(self):
        """
        Getter Function  for width attribute
        Return
         returns width of  rectangle class/object

        """
        return self.__width___
    @width.setter
    def width(self, value):
        """
        Setter Function for width atribute
        Returns : void
        """
        if not  isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
                raise ValueError("width must be >=0")
        self.__width__ = value
    @property
    def height(self):
        """
        Getter Function  for width attribute
        Return
        returns height of  rectangle clas

        """
        return self.__height___

    @height.setter
    def height(self, value):
        """
        Setter Function for height atribute
        Returns : void
        """
        if not  isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
                raise ValueError("width must be >= 0 ")
        self.__height__ = value
