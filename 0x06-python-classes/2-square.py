#!/usr/bin/python3

class Square:
    """square class with exceptions"""

    def __init__(self, size=0):
        """initializing"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >=0')
        else:
            self.__size = size
