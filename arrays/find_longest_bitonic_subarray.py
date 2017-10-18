"""The longest bitonic subarray problem is to find a subarray of a given sequence in which 
the subarray's elements are first sorted in in increasing order, then in in decreasing order,
and the subarray is as long as possible. Strictly ascending or descending subarrays are
also accepted."""


def longest_bitonic(arr):
    """Straightforward approach of O(N) time and O(1) space.

    Args:
        arr: an array of integers.

    Returns:
        Longest bitonic subarray.
    """
    max_start = 0
    max_len = 0
    i = 0
    while i < len(arr) - 1:
        istart = i
        while i < len(arr) - 1 and arr[i] < arr[i+1]:
            i += 1
        while i < len(arr) - 1 and arr[i] > arr[i+1]:
            i += 1
        if (i - istart + 1) > max_len:
            max_len = (i - istart + 1)
            max_start = istart
        while i < len(arr) - 1 and arr[i] == arr[i+1]:
            i += 1
    return arr[max_start:(max_start + max_len)]
    
if __name__ == '__main__':
    assert []              == longest_bitonic([])
    assert [1,2,3,4,5]     == longest_bitonic([1,2,3,4,5])
    assert [5,4,3,2,1]     == longest_bitonic([5,4,3,2,1])
    assert [1, 2, 1]       == longest_bitonic([1, 2, 1, 2, 1, 2, 1, 2, 1])
    assert [1, 2, 3, 2, 1] == longest_bitonic([1, 2, 1, 2, 3, 2, 1]), longest_bitonic([1, 2, 1, 2, 3, 2, 1])
    assert [1, 2, 1]       == longest_bitonic([1, 1, 1, 2, 1, 3]) 
    assert [1, 2, 3, 2, 1] == longest_bitonic([1, 2, 3, 2, 1, 2, 3])
