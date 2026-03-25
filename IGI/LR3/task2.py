'''
Laboratory work number: 3. Standard data types, collections, functions, modules.
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.03.2026.

This module contains realisation of input and substraction function.
'''



import ui

def main():
    """
    Main function that repeatedly subtracts user-provided integers from 10000.

    Prompts the user to enter integers one by one. Each entered integer is
    subtracted from the current result, which starts at 10000. After x becoming
    less than 0< loop stops and the current result in printed
    """
    cur_res = 10000
    while cur_res >= 0:
        cur_num = ui.read_int("Enter an integer ")
        cur_res -= cur_num

    print(f"Result is {cur_res}")