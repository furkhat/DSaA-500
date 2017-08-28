"""Given an array containing only 0's, 1's and 2's, sort the array in linear time using constant space."""


def sort_linear(A):
    """Sorts array using 3-way partitioning in a linear time.

    Args:
        A: Array containing only 0's, 1's and 2's.
    """
    pivot = 1
    i = 0
    j = 0
    r = len(A) - 1
    while j <= r:
        if A[j] > pivot:
            A[r], A[j] = A[j], A[r]
            r -= 1
        elif A[j] == pivot:
            j += 1
        else:
            A[j], A[i] = A[i], A[j]
            i += 1
            j += 1

if __name__ == '__main__':
    import random
    n = 100
    for _ in range(n):
        A = [random.randint(0, 2) for __ in range(n)]
        expected = sorted(A)
        sort_linear(A)
        assert expected == A
