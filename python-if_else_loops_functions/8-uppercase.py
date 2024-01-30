#!/usr/bin/python3
def uppercase(str):
    n = ""
    for i in str:
        if ((ord(i) >= 97) and (ord(i) <= 122)):
            n += chr(ord(i) - 32)
        else:
            n += i
    print("{}".format(n))