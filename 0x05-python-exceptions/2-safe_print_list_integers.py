#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for item in my_list:
            try:
                if i < x:
                    print("{:d}".format(item), end='')
                    i += 1
            except: 
                pass
        print()
    except (ValueError, TypeError):
        pass
    finally:
        return i
