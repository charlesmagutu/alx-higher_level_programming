#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    for x in my_list:
        l = []
        if x % 2 == 0:
            l.append(True)
        else:
            l.append(False)
        return l
