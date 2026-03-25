import list_initialization
import ui


def find_min_neg_ind(list):
    """
    Finds the index of the minimum negative element in the list.

    Uses min() with a key to locate the smallest value in the list.
    If that smallest value is negative, returns its index.
    Otherwise, returns -1 indicating no negative elements exist.

    Parameters:
        list (list of int/float): The list to search.

    Returns:
        int: Index of the smallest negative element, or -1 if no negatives.
    """
    ind, val = min(enumerate(list), key = lambda x : x[1])
    if val < 0:
        return ind
    else:
        return -1
    

def find_sum(list):
    """
    Computes the sum of elements between the first and second negative elements.

    Finds the indices of the first two negative numbers in the list.
    Then sums all elements strictly between those indices (excluding the negatives themselves).
    If fewer than two negative elements exist, returns 0.

    Parameters:
        list (list of int/float): The input list.

    Returns:
        int/float: Sum of elements between the first and second negative elements.
    """
    ind1 = -1
    ind2 = -1
    for i in range(len(list)):
        if (ind1 != -1 and list[i] < 0):
            ind2 = i
            break
        if (list[i] < 0):
            ind1 = i

    sum = 0
    for i in range(ind1 + 1, ind2):
        sum += list[i]   

    return sum 
    

def main():
    """
    Main entry point of the program.

    Initializes a list using list_initialization.initialize_list(),
    prints the list, finds the index of the minimum negative element,
    and computes the sum of elements between the first two negative elements.
    Displays the results or appropriate messages if conditions are not met.
    """
    list = list_initialization.initialize_list()

    min_neg_ind = find_min_neg_ind(list)
    sum_btw_neg_1_ans_2 = find_sum(list)

    print(list)

    if min_neg_ind != -1:
        print(f"Minimum negative element index is {min_neg_ind}")
    else:
        print("There are no negative elements in the list")
    print(f"Sum of elements between 1 and 2 negative elements is {sum_btw_neg_1_ans_2}")