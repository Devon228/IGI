import sys


def looped_input(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                print("Invalid input. Try again.")
            except EOFError:
                print("byeeeeeee!")
                sys.exit(0)

    return wrapper


def bound_input(func):
    def wrapper(*args, **kwargs):
        min = kwargs.pop("min", None)
        max = kwargs.pop("max", None)
        ranges = kwargs.pop("ranges", None)

        val = func(*args, **kwargs)

        if ranges is not None:
            for r in ranges:
                if val > r[0] and val < r[1]:
                    return val
            raise ValueError(f"Value must be in {ranges}")

        if min is not None and val < min:
            raise ValueError(f"Value must be at least {min}")

        if max is not None and val > max:
            raise ValueError(f"Value must be at most {max}")

        return val

    return wrapper


@looped_input
@bound_input
def read_int(prompt):
    val_str = input(prompt)
    val = int(val_str)
    return val


@looped_input
@bound_input
def read_float(prompt):
    val_str = input(prompt)
    val = float(val_str)
    return val


@looped_input
def read_str(prompt):
    val_str = input(prompt)
    if val_str == "":
        raise ValueError("Empty string")
    return val_str


@looped_input
def read_float_list(prompt):
    val_str = input(prompt)
    val = [float(f) for f in val_str.split()]
    if len(val) == 0:
        raise ValueError("Empty list")
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
                str_col = f"{col:.6f}"
            else:
                str_col = str(col)

            print("| " + str_col.ljust(8), end=" ")
        print("|")
