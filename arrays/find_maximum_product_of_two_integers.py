"""Given an array of integers, find maxumum product of two integers in an array."""

def max_product_naive(A):
    """A naive O(n^2) solution that check every possible pair.

    Args:
        A: An array of integers.

    Returns:
        The maxumum product of two integers in an array.
    """

    assert len(A) >= 2

    max_product = A[0] * A[1]
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] * A[j] > max_product:
                max_product = A[i] * A[j]
    return max_product

def max_product_linear(A):
    """A naive O(n^2) solution that check every possible pair.

    Args:
        A: An array of integers.

    Returns:
        The maxumum product of two integers in an array.
    """

    assert len(A) >= 2

    max1 = max(A[0], A[1])
    min1 = min(A[0], A[1])
    max2 = min1
    min2 = max1

    for i in range(2, len(A)):
        if A[i] >= max1:
            max2 = max1
            max1 = A[i]
        elif A[i] > max2:
            max2 = A[i]

        if A[i] <= min1:
            min2 = min1
            min1 = A[i]
        elif A[i] < min2:
            min2 = A[i]

    return max(min1 * min2, max1 * max2)

if __name__ == '__main__':
    import random
    n = 100
    for __ in range(1000):
        A = [random.randint(-1000, 1000) for _ in range(n)]
        assert max_product_naive(A) == max_product_linear(A)
