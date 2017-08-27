"""Given an array of integers, find maximum length sub-array having given sum."""


def find_naive(arr, value):
    """Naive O(n^2) solution.

    Args:
        arr: An array of integers.
        value: The Value for sum.

    Returns:
        Maximum length sub-array having given sum.
    """
    s = 0
    ans = (0, -1)
    for i, _ in enumerate(arr):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s == value and (j - i) > (ans[1] - ans[0]):
                ans = (i, j)

    return arr[ans[0]:(ans[1]+1)]


def find_memo(arr, value):
    """An O(N) solution using memoization of sum indeces.

    Args:
        arr: An array of integers.
        value: The Value for sum.

    Returns:
        Maximum length sub-array having given sum.
    """
    ans = (0, 0)
    s = 0
    sums = {0: -1}
    for i, item in enumerate(arr):
        s += item
        k = s - value
        if k in sums and (i - sums[k]) > (ans[1] - ans[0]):
            ans = (sums[k]+1, i+1)
        sums[s] = sums.get(s, i)
    return arr[ans[0]:ans[1]]

if __name__ == '__main__':
    import random
    n = 100
    for _ in range(1000):
        arr = [random.randint(-100, 100) for __ in range(n)]
        value = random.randint(-500, +500)
        try:
            assert find_naive(arr, value) == find_memo(arr, value)
        except AssertionError:
            print(value)
            print(arr)
            print(find_naive(arr, value))
            print(find_memo(arr, value))
            break
