#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for c in str:
        if ord(c) >=97 and ord(c) <=122:
            upper +=chr(ord(c) - 32)
        elif c == " ":
            upper +=c
        else:
            upper +=c
    print("{}".format(upper))
