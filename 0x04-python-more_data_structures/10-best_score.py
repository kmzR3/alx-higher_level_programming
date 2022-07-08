#!/usr/bin/python3
# Write a function that returns a key with the biggest integer value.
def best_score(a_dictionary):
    max_value = 0
    for key in a_dictionary:
        if a_dictionary[key] > max_value:
            max_value = a_dictionary[key]
            max_key = key
    return max_key
    