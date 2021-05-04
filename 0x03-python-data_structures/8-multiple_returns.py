#!/usr/bin/python3
def multiple_returns(sentence):
    mytup = ()
    if len(sentence) == 0:
        mytup = 0, "None"
    else:
        mytup = len(sentence), sentence[0]
    return mytup
