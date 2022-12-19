#!/usr/bin/python3
def safe_print_integer(value):
    try:
        x = 1
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        x = 0
        return False 
    finally:
        return bool(x)
