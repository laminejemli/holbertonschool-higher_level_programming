#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = set(my_list)
    rest = 0
    for i in n:
        rest += i
    return rest
