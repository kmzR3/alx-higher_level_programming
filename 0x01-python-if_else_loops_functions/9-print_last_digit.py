#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        last_digit = number % 10
        print(last_digit)
    elif number < 0:
        last_digit = number % -10
        print(last_digit)
    else:
        print(0)


