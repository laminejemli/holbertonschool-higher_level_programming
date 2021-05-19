#!/usr/bin/python3
""" module into classes """


class Square():
    """ class Square that defines a square """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError
        if size < 0:
            raise ValueError
        self.__size = size
