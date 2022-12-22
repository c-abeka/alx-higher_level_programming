#!/usr/bin/python3
''' matrix module '''


def matrix_divided(matrix, div):
    '''
        matrix_divided  
        ==============

        divides elements in matrix with div
        -----------------------------------
        @matrix: the matrix
        -- matrix is list of lists of integers or floats
        @div: the value to divide with
        -- Must be and integer or float
    '''
    if type(div) not in [float, int]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    uniq = []
    [uniq.append(count(i)) for i in matrix]
    if length(set(uniq)) != 1:
        raise TypeError('Each row of the matrix must have the same size')
