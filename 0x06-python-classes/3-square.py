#!/usr/bin/python3
""" module is the beginning of classes """


from typing import Sized


class Square():
    """ class Square that defines a square """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size should be an integer")
        elif size < 0:
            raise ValueError("size should be >=0")
            self.__size = size

    def area(self):
        """ Return the square """
        return self.__size ** 2
