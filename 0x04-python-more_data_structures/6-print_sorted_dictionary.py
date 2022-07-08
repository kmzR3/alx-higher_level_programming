#!/usr/bin/python3
# Write a function that prints a dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print(key, a_dictionary[key])
        