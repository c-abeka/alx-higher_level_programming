#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for el in my_list:
            if i < x:
                print("{}".format(el), end='')
                i += 1
        print()
        return i
    except Exception:
        raise
    finally:
        return i
