#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord(L): None for L in 'cC'})
    return new_string
