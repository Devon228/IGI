import sys


def looped_input(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                print("Invalid input. Try again.")
            except EOFError:
                print("End of file. Exit")
                sys.exit(0)

    return wrapper


def bound_input(func):
    def wrapper(*args, **kwargs):
        min = kwargs.pop("min", None)
        max = kwargs.pop("max", None)
        strict_min  = kwargs.pop("strict_min", None)
        strict_max = kwargs.pop("strict_max", None)

        val = func(*args, **kwargs)

        if min is not None and val < min:
            raise ValueError(f"Value must be at least {min}")

        if max is not None and val > max:

            raise ValueError(f"Value must be at most {max}")
        if strict_min is not None and val <= strict_min:
            raise ValueError(f"Value must be greater then {strict_min}")

        if strict_max is not None and val >= strict_max:
            raise ValueError(f"Value must be less then {strict_max}")

        return val

    return wrapper


@looped_input
@bound_input
def read_int(msg):
    val_str = input(msg)
    val = int(val_str)
    return val


@looped_input
@bound_input
def read_float(msg):
    val_str = input(msg)
    val = float(val_str)
    return val
import sys


@looped_input
def read_str(msg):
    val_str = input(msg)
    if val_str == "":
        raise ValueError("Empty string")
    return val_str


@looped_input
def read_float_list(msg, sz):
    val_str = input(msg)
    val = [float(f) for f in val_str.split()]
    if len(val) == 0:
        raise ValueError("Empty list")
    if len(val) != sz:
        raise ValueError("Must be sz elements in input")
    return val


def show_table(iterable, header=[]):
    for h in header:
        print("| " + h.ljust(8), end=" ")
    print("|")
    for h in header:
        print("|-" + "-" * 8, end="-")
    print("|")

    for row in iterable:
        for col in row:
            str_col = None
            if isinstance(col, float):
                str_col = f"{col:.5f}"
            else:
                str_col = str(col)

            print("| " + str_col.ljust(8), end=" ")
        print("|")