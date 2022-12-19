#!/usr/bin/python3
def safe_print_integer(value):
    x = 1
    try:
        val = int(value)
        print("{:d}".format(val))
        return True
    except ValueError:
        x = 0
    finally:
        return bool(x)
