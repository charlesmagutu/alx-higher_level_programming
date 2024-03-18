#!/usr/bin/python3


def multiple_returns(sentence):
    ln = len(sentence)
    if ln > 0:
        first = sentence[0]
        return ln,first
    return ln, None

