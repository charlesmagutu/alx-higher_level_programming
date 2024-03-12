#!/usr/bin/python3
def islower(c):
    for char in c:
        if ord('a') <= ord(char) <= ord('z') or char.isdigit():
            return True
    return False
