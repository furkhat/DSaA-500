"""Given an array of integers, find all subarrays having 0 sum."""


def find_naive(arr):
    """Naive O(n^3) solution.

    Args:
        arr: An array of integers.

    Returns:
        Array of all subarrays having 0 sum.
    """
    result = []
    s = 0
    for i, _ in enumerate(arr):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s == 0:
                result.append(arr[i:j+1])

    return result


def find_memo(arr):
    """An O(N^2) solution using memoization of sum indeces.

    Args:
        arr: An array of integers.

    Returns:
        Array of all subarrays having 0 sum.
    """
    result = []
    s = 0
    sums = {}
    sums[0] = [-1]
    for i, item in enumerate(arr):
        s += item
        sums[s] = sums.get(s, [])
        for index in sums[s]:
            result.append(arr[index+1:i+1])
        sums[s].append(i)
    return result

if __name__ == '__main__':
    import random
    n = 100
    for _ in range(100):
        arr = [random.randint(-100, 100) for __ in range(n)]
        try:
            assert sorted(find_naive(arr)) == sorted(find_memo(arr))
        except AssertionError:
            print(arr)
            break
