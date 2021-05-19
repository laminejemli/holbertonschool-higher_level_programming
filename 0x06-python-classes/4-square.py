#!/usr/bin/python3
class Square:
    """ Represents a square.
    Private instance attribute: size:
    Instantiation with optional size.
    Public instance method: def area(self).
    """

    def __init__(self, size=0):
        """ Initializes size """
        self.__size = size

    @property
    def size(self):
        """ Retrieves the data. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size. """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the square area. """
        return self.__size ** 2
