"""Given an array of integers, rearrange the array such that every second element of the
array is greater then its left and right elements. Assume no duplicate elements are
present in the array."""

def rearrange(A):
    """Solves in O(n) time. Simple procedure, the trick is the proof.

    Args:
        A: Array of integers.

    Returns:
        The input array.
    """
    
    odd_step = True
    for i in range(len(A) - 1):
        if (A[i] > A[i+1]) == odd_step:
            A[i], A[i+1] = A[i+1], A[i]
        odd_step = not(odd_step)
    return A

if __name__ == '__main__':
    assert rearrange([1,2,3,4,5,6,7]) == [1,3,2,5,4,7,6]
    assert rearrange([9, 6, 8, 3, 7]) == [6, 9, 3, 8, 7]
    assert rearrange([6, 9, 2, 5, 1, 4]) == [6, 9, 2, 5, 1, 4]
