#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    r = 0
    for l in range(1, len(sys.argv)):
        r += int(sys.argv[l])
    print("{}".format(r))
