#!/usr/bin/python3
for T in range(ord('a'), ord('z') + 1):
    if T != ord('e') and T != ord('q'):
        print("{:c}".format(T), end="")
