#!/usr/bin/python3
# Write a function that returns a new dictionary with all values multiplied by 2
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key in a_dictionary:
        new_dictionary[key] = a_dictionary[key] * 2
    return new_dictionary
    