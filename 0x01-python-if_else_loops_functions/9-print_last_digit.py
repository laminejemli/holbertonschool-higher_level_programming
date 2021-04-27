#!/usr/bin/python3
def uppercase(str):
    for l in str:
        if ord(l) >= ord('a') and ord(l) <= ord('z'):
            char = chr(ord(l) - 32)
        else:
            char = l
        print("{:s}".format(char), end="")
    print('')
