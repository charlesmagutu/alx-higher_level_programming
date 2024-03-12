#!/usr/bin/python3
def print_last_digit(number):
    res = ""
    if number > 0:
        res += str(number % 10)
    elif number == 0:
        res += str(number)
    else:
        res += str(abs(number) % 10)
    print(res)
