#!/usr/bin/python3
def inherits_from(obj, a_class):
    if isinstance(obj, a_class) ans\
            issubclass(a_class, obj.__class__) is False:
        return True
    return False
