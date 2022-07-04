#!/usr/bin/python3
# Write a function that prints a matrix of integers
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for col in range(len(line)):
            print(
                "{:d}".format(line[col]),
                end="" if col == len(line) - 1 else " ")
        print("")    
