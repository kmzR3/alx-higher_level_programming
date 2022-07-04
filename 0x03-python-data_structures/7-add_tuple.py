#!/usr/bin/python3
# Write a function that adds 2 tuples.
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        return tuple_b
    if len(tuple_b) == 0:
        return tuple_a
    return tuple_a + tuple_b
    