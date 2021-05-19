#!/usr/bin/python3
""" module is the beginning of classes """


class Square():
    """ class Square that defines a square """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size an integer")
        if size < 0:
            raise ValueError("size >= 0")
        self.__size = size

        def area(self):
            """ end and return """
        return self.__size ** 2
