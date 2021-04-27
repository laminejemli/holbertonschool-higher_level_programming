#!/usr/bin/python3
def uppercase(str):
    for U in str:
        if ord(U) >= ord('a') and ord(U) <= ord('z'):
            char = chr(ord(U) - 32)
        else:
            char = U
        print("{:s}".format(char), end="")
    print('')
