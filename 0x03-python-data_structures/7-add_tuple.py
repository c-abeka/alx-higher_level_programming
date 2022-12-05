#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2, b1, b2 = (0, 0, 0, 0)
    len1 = len(tuple_a)
    len2 = len(tuple_b)

    if len1 == 2:
        a1, b1 = tuple_a
    if len2 == 2:
        a2, b2 = tuple_b
    if len1 == 1:
        a1 = tuple_a[0]
    if len2 == 1:
        a2 = tuple_b[0]
    return a1 + a2, b1 + b2
