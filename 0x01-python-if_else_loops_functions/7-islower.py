#!/usr/bin/python3
def islower(c):
    if ord(c) > 96 and ord(c) < 173:
        return True
    elif ord(c) > 64 and ord(c) < 133:
        return False
    elif ord(c) >= 0 and ord(c) < 10:
        return False
