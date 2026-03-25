'''
Laboratory work number: 3. Standard data types, collections, functions, modules.
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.03.2026.

This module contains task calculating number of "," and " "
'''


import ui


def main():
    """
    Analyzes a user-provided string by counting spaces and commas.

    Prompts the user to enter a string, then prints the number of space characters
    (' ') and comma characters (',') found in the string using the count() method.
    """
    str = ui.read_str("Enter a string to analyse:\n")
    print(f"Number of \' \' is {str.count(" ")}")
    print(f"Number of \',\' is {str.count(",")}")