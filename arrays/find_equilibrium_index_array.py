"""Given an array of integers, find equilibrium index in it."""

def equilibrium_index(A):
    """Solves the problem in O(n) time and constant space.

    Args:
        A: An array of integers
    
    Returns:
        First equilibrium index if any or -1.
    """

    left_sum = 0
    right_sum = sum(A)
    for i, val in enumerate(A):
        right_sum -= val
        if right_sum == left_sum:
            return i
        left_sum += val
    return -1        

if __name__ == '__main__':
    assert -1 == equilibrium_index([])
    assert  0 == equilibrium_index([0, -3, 5, -4, -2, 3, 1, 0])
    assert -1 == equilibrium_index([0, 1, 2, 3, 4])
    assert  3 == equilibrium_index([0, 1, 2, 0, 3])

