#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx > 0:
        my_list[idx] = element
    elif idx < 0:
        return my_list
    return my_list
