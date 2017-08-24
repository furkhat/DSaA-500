"""Given an binary array, sort it in linear time and constant space.
Output should contains all zeroes followed by all ones."""

def sort_by_counting(arr):
    """Counts number of zeros and ones and fills
    all zeros and then all ones in the array.

    Args:
        arr: An array containing zeros and ones.
    """
    zeros_count = arr.count(0)
    for i in range(zeros_count):
        arr[i] = 0
    for i in range(zeros_count, len(arr)):
        arr[i] = 1
    return arr

def sort_by_placing_zeros_in_front(arr):
    """Iterates over the array and puts all zeros in front of the array.
    The rest filled with ones.

    Args:
        arr: An array containing zeros and ones.
    """
    next_zeros_index = 0
    for i, arr_i in enumerate(arr):
        if arr_i == 0:
            arr[next_zeros_index] = 0
            next_zeros_index += 1
    for i in range(next_zeros_index, len(arr)):
        arr[i] = 1
    return arr

def sort_with_partitioning(arr):
    """Sorts by applying a bit modified version of quicksort partitioning logic.

    Args:
        arr: An array containing zeros and ones.
    """
    pivot = 1
    j = 0
    for i, arr_i in enumerate(arr): 
        if arr_i < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

if __name__ == '__main__':
    import random

    def test_function(f):
        for _ in range(100):
            n = 100
            arr = [random.randint(0, 1) for _ in range(n)]
            sorted_arr = sorted(arr)
            assert f(arr) == sorted_arr
    
    test_function(sort_by_counting)
    test_function(sort_by_placing_zeros_in_front)
    test_function(sort_with_partitioning)
