"""Given an unsorted array of integers, find pair with given sum in it."""
import bisect


def find_naive(arr, value):
    """Naive O(n^2) way.

    Args:
        arr: An unsorted array of integers.
        value: The value of sum.

    Returns:
        The indeces of two items that sum to given value or None.
    """
    for i, arr_i in enumerate(arr):
        for j in range(i+1, len(arr)):
            if arr_i + arr[j] == value:
                return i, j

def find_with_bisect(arr, value):
    """O(nlogn) solution that uses sorting and binary search.

    Args:
        arr: An unsorted array of integers.
        value: The value of sum.

    Returns:
        The indeces of two items that sum to given value or None.
    """
    arr = sorted(arr)
    for i, first in enumerate(arr):
        j = bisect.bisect_right(arr, value - first)
        second = arr[j]
        if second + first == value:
            return i, j

def find_lenear(arr, value):
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
            return index_by_value[value - first], i
        index_by_value[first] = i
