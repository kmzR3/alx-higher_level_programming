#!/usr/bin/python3
# Write a function that prints all integers of a list, in reverse orde
def print_reversed_list_integer(my_list=[]):
    for i in reversed(my_list):
        print("{:d}".format(i))
    return None
