#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for i in item:
            print("{}".format(i), end=' ')
        print("")
