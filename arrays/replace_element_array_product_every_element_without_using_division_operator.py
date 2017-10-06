"""Given an array of integers, replace each element of the array with product of every other
element in the array without using division operator."""


def replace_with_self_exclusive_product(arr):
    """Linear algorithm to replace each element with product of all other elements
    without using division operator.

    Args:
        arr: an nonempty array of numbers. 

    Returns:
        A modified copy of the array.
    """
    arr = list(arr)

    right_to_left_products = [1] * len(arr)
    p = 1
    for i in range(len(arr) - 1, -1, -1):
        p *= arr[i]
        right_to_left_products[i] = p

    p = 1
    for i in range(len(arr) - 1):
        p, arr[i] = p * arr[i], p * right_to_left_products[i+1]
    arr[-1] = p

    return arr

def naive(arr):
    """A simple correct algorithm to solve the problem used in stress testing.

    Args:
        arr: an nonempty array of numbers. 

    Returns:
        A modified copy of the array.
    """
    result = list(arr)

    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i == j:
                continue
            product *= arr[j]
        result[i] = product

    return result

if __name__ == '__main__':
    import random

    n = 10 
    ntests = 100
    for _ in range(ntests):
        arr = [random.randint(1, 100) for i in range(n)]
        try:
            naive_result = naive(arr)
            solution_result = replace_with_self_exclusive_product(arr)
            assert naive_result == solution_result
        except AssertionError:
            print("Failed for array: ", arr)
            print("Expected result: ", naive_result)
            print("Solution result: ", solution_result)
            break
