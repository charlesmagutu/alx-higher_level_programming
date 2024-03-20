#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_lis = my_list[:]
    for i in range(len(my_list)):
        if new_lis[i] == search:
            new_lis[i] = replace
    return new_lis
