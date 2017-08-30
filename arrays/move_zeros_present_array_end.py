"""Given an array of integers, move all zeros present in the array to the end.
The solution should maintain the relative order of items in the array."""

def move_zeros(A):
    """O(n) time and constant space solution.

    Args:
        A: Array of integers.
    """    
    place_index = 0
    for i, val in enumerate(A):
        if val is not 0:
            A[i], A[place_index] = A[place_index], A[i]
            place_index += 1

if __name__ == '__main__':
    def test_for_case(initial, expected):
        move_zeros(initial)
        assert initial == expected

    test_for_case([], [])
    test_for_case([1], [1])
    test_for_case([1, 0], [1, 0])
    test_for_case([0, 1], [1, 0])
    test_for_case([6, 0, 8, 2, 3, 0, 4, 0, 1], [6, 8, 2, 3, 4, 1, 0, 0, 0])
