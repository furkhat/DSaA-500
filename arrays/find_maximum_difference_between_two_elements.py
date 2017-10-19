"""Given an array of integers, find the maximum difference between two elements in the
array such that smaller element appears before the larger element."""

def find(arr):
    """O(n) time and constant space solution.

    Args:
        arr: a non empty array of integers.

    Returns:
        A pair of element with max difference.
    """
    cur_min = arr[0]
    max_diff = 0
    result = None
    for i, x in enumerate(arr):
        if x < cur_min:
            cur_min = x
        elif x - cur_min > max_diff:
            max_diff = x - cur_min
            result = (cur_min, x)
    return result

def find_brute_force(arr):
    """Collect all the pairs, and chose best. O(n^2) time and O(n^2) space solution.

    Args:
        arr: an array of integers.

    Returns:
        A pair of element with max difference or None.
    """
    pairs = [(arr[i], arr[j]) for i in range(len(arr)) for j in range(i+1, len(arr)) if arr[i] < arr[j]]
    return max(pairs, key=lambda pair: pair[1] - pair[0])

if __name__ == '__main__':
    import random
    n = 10
    ntests = 100
    for _ in range(ntests):
        arr = [random.randint(0, 10**5) for __ in range(n)]
        fast_result = find(arr)
        brute_force_result = find_brute_force(arr)
        assert fast_result == brute_force_result, "fast:" + str(fast_result) + ", brute force:" + str(brute_force_result) + ", array:" + str(arr)
