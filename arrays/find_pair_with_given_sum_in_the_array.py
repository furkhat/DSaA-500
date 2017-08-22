"""Given an unsorted array of integers, find pair with given sum in it."""
import bisect


def find_naive(arr, value):
    """Naive O(n^2) way.

    Args:
        arr: An unsorted array of integers.
        value: The value of sum.

    Returns:
        The two items that sum to given value or None.
    """
    for i, arr_i in enumerate(arr):
        for j in range(i+1, len(arr)):
            if arr_i + arr[j] == value:
                return arr[i], arr[j]

def find_with_bisect(arr, value):
    """O(nlogn) solution that uses sorting and binary search.

    Args:
        arr: An unsorted array of integers.
        value: The value of sum.

    Returns:
        The two items that sum to given value or None.
    """
    arr = sorted(arr)
    for i, first in enumerate(arr):
        second = value - first
        j = bisect.bisect_right(arr, second)
        if j < len(arr) and j > 0 and j-1 != i and arr[j-1] == second:
            return arr[i], arr[j-1]

def find_with_two_pointers(arr, value):
    """O(nlogn) solution that uses sorting.

    Args:
        arr: An unsorted array of integers.
        value: The value of sum.

    Returns:
        The two items that sum to given value or None.
    """
    arr = sorted(arr)
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < value:
            left += 1
        elif arr[left] + arr[right] > value:
            right -= 1
        else:
            return arr[left], arr[right]

def find_linear(arr, value):
    """O(n) solution using has table.

    Args:
        arr: An unsorted array of integers.
        value: The value of sum.

    Returns:
        The indeces of two items that sum to given value or None.
    """
    index_by_value = {}
    for i, first in enumerate(arr):
        if value - first in index_by_value:
            return value - first, arr[i]
        index_by_value[first] = i


if __name__ == '__main__':
    import random
    for _ in range(100):
        arr = [random.randint(0, 100) for _ in range(100)]
        value = random.randint(0, 50)
        try:
            naive = find_naive(arr, value)
            with_bisect = find_with_bisect(arr, value)
            with_two_pointers = find_with_two_pointers(arr, value)
            linear = find_linear(arr, value)
            if all([naive, with_bisect, linear, with_two_pointers]):
                assert sum(naive) == sum(with_bisect) == sum(linear) == sum(with_two_pointers) == value
            else:
                assert any([naive, with_bisect, linear, with_two_pointers]) == False
        except AssertionError:
            print(arr)
            print(value)
            print(naive)
            print(with_bisect)
            print(linear)
            break
