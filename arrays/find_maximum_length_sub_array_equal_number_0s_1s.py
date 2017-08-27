"""Given an binary array containing 0 and 1, find maximum length sub-array having equal number of 0's and 1's.
The idea to the solution of this problem is to generealize it to the problem
of finding max length sub-array having 0 sum. We just treat all 0's as -1.
"""

def find_naive(A):
    """A naive O(n^2) time.

    Args:
        A: an array consisting of 0's and 1's.

    Returns:
        Maximum length sub-array with equal numers of 0's and 1's.
    """
    ans = (0, 0)
    for i in range(len(A)):
        s = 0
        for j in range(i, len(A)):
            s += A[j] if A[j] == 1 else -1
            if s == 0 and (j - i) > (ans[1] - ans[0]):
                ans = (i, j+1)
    return A[ans[0]:ans[1]]

def find_memo(A):
    """A O(n) time implementation using O(n) space.

    Args:
        A: an array consisting of 0's and 1's.

    Returns:
        Maximum length sub-array with equal numers of 0's and 1's.
    """
    ans = (0, 0)
    cache = {0: -1}
    current_sum = 0
    for i, item in enumerate(A):
        current_sum += item if item == 1 else -1
        if current_sum in cache and i - cache[current_sum] > ans[1] - ans[0]:
            ans = (cache[current_sum] + 1, i + 1)
        cache[current_sum] = cache.get(current_sum, i)
    return A[ans[0]:ans[1]]

if __name__ == '__main__':
    import random
    n = 100
    for _ in range(1000):
        A = [random.randint(0, 1) for __ in range(n)]
        assert find_naive(A) == find_memo(A)
