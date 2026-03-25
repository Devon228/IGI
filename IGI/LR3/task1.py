'''
Laboratory work number: 3. Standard data types, collections, functions, modules.
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.03.2026.

This module contains calculation method for row ln(1-x).
'''



import math
import ui

def row_generator (x):
    """
    Generator of series terms for computing ln(1 - x).

    Yields tuples (n, partial_sum), where partial_sum is the partial sum
    of the series -x - x^2/2 - x^3/3 - ... for the given x.
    Generation continues up to n = 500 (loop limit).

    Parameters:
        x (float): Argument for which the series is computed. |x| < 1.

    Yields:
        tuple: (term index n, partial sum up to n).
    """
    cur_n = 1
    cur_num = x
    cur_sum = -cur_num

    while cur_n < 500:   
        yield (cur_n, cur_sum)
        cur_n += 1
        cur_num = (cur_num * x) * ((cur_n - 1) / cur_n)
        cur_sum += -cur_num


def calculate_row_sum(x):
    """
    Computes the exact value of ln(1 - x) using math.log.

    Parameters:
        x (float): Argument for the logarithm. |x| < 1.

    Returns:
        float: The value of ln(1 - x).
    """
    return math.log(1 - x)

def table_generator(x, eps, row_sum):
    """
    Generator of table rows showing convergence of the series.

    For each term from row_generator, calculates the absolute error
    relative to the exact value row_sum. Stops when error <= eps.

    Parameters:
        x (float): Argument of the series.
        eps (float): Required precision.
        row_sum (float): Exact value of ln(1 - x).

    Yields:
        tuple: (x, n, partial_sum, exact_sum, error).
    """
    for cur_n, cur_val in row_generator(x):
        cur_precision = abs(cur_val - row_sum)
        yield(x, cur_n, cur_val, row_sum, cur_precision)
        if cur_precision <= eps:
            break

def main():
    """
    Main function of the program.

    Prompts the user for x (|x| < 1) and precision eps.
    Computes the exact value of ln(1 - x) and displays a table
    showing the convergence of partial sums to that value.
    """
    x = ui.read_float("Enter x for computing ln(1 - x), |x| < 1\n", strict_min = -1.0, strict_max = 1.0)
    eps = ui.read_float("Enter precision of computing row eps:\n", min = 1e-9, max = 1)

    row_sum = calculate_row_sum(x)
    ui.show_table(table_generator(x, eps, row_sum), ["x", "n", "F(x)", "sum", "eps"])