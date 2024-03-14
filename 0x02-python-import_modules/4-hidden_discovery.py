#!/usr/bin/python3
import hidden_4


def check():
    for a in dir(hidden_4):
        if a[:2] != '__':
            print("{:s}".format(a))


if __name__ == '__main__':
    check()
