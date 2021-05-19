#!/usr/bin/python3
"""class that Defines a class Square"""


class Square:
    """Defines a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Sets the square
        Attributes:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """SUM of  the square's area
        Returns:
            the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """get the value of __size
        Returns:
            The value of the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets of __size
        Attributes:
            value (int): the size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size should be an integer")
        else:
            if value < 0:
                raise ValueError("size should be >= 0")
            else:
                self.__size = value
