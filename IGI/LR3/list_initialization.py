'''
Laboratory work number: 3. Standard data types, collections, functions, modules.
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.03.2026.

This module contains list initialization with input or generator.
'''



import ui
import random


def get_list_from_user(sz):
    list = ui.read_float_list("Enter list elements:\n", sz)
    return list

def get_list_from_generator(sz, l, r):
    for _ in range(sz):
        yield random.uniform(l, r)

def initialize_list():
    list_len = ui.read_int("Enter a positive list size\n", min=1)

    print("Choose option to enter list")
    print("1. Enter list manually")
    print("2. Generate list")
    option = ui.read_int("Enter option ", min=1, max=2)

    if option == 1:
        return get_list_from_user(list_len)
    else:
        return list(get_list_from_generator(list_len, -10, 10))