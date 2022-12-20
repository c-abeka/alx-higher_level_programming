#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(list_length):
        try:
            div = my_list_1[x] / my_list_2[x]
        except IndexError:
            div = 0
            print('out of range')
        except ZeroDivisionError:
            div = 0
            new_list.append(0)
        except (TypeError, ValueError):
            div = 0
            print('wrong type')
        finally:
            new_list.append(div)
    return new_list
