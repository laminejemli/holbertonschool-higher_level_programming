#!/usr/bin/python3
class Square:
    """ into the module class """

    def __init__(self, size=0):
        """ set the data."""
        if not isinstance(size, int):
            raise TypeError("size an integer")
        elif size < 0:
            raise ValueError("size >= 0")
        self.__size = size

    def area(self):
        """ Returns the square  """
        return self.__size ** 2
