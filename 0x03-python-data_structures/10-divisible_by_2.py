#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    for x in my_list:
        lis = []
        if x % 2 == 0:
            lis.append(True)
        else:
            lis.append(False)
        return lis
