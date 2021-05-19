#!/usr/bin/python3
class Square:
    """Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Private instance attribute: position:
        - property def position(self)
        - property setter def position(self, value)
    Instantiation with optional size and optional position.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """

    def __init__(self, size=0, position=(0, 0)):
        """ set the data. """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Retrieve the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ size to a value. """
        if not isinstance(value, int):
            raise TypeError("size an integer")
        elif value < 0:
            raise ValueError("size >= 0")
        self.__size = value

    @property
    def position(self):
        """ Retrieve the position """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a  2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a  2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a  2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #,
        at the position given """

        if self.__size == 0:
            print()
            return
        for l in range(0, self.__position[1]):
            print()
        for a in range(0, self.__size):
            for z in range(0, self.__position[0]):
                print(" ", end="")
            for v in range(0, self.__size):
                print("#", end="")
            print()
