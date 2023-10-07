#!/usr/bin/python3
#Auth: EL HADDOUMI Mohammed
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for x in reversed(my_list):
            print("{:d}".format(x))
