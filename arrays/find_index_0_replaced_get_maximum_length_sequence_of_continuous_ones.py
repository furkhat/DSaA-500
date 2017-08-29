"""Given a binary array, find the index of 0 to be replaced with 1 to get maximum
length sequence of continuous ones."""

def find_index(A):
    """Solves the problem in O(n) by maintaining number of 1 before each zero
    and maximizing the number of ones by replacing previous zero.

    Args:
        A: Array of ones and zeros.

    Returns:
        The index of the item to be replaced.
    """
    best = 0
    ans = -1
    prev_ones = -1
    ones = 0

    for i, item in enumerate(A):
        if item == 1:
            ones += 1
        else:
            if prev_ones + 1 + ones > best:
                best = prev_ones + 1 + ones
                ans = i - ones - 1
            prev_ones = ones
            ones = 0
    if prev_ones != -1 and prev_ones + 1 + ones > best:
        best = prev_ones + 1 + ones
        ans = len(A) - ones - 1
    return ans

def find_index2(A):
    """Solves the problem in O(n) by maintaining number of 1 obtained by replacing last zero.

    Args:
        A: Array of ones and zeros.

    Returns:
        The index of the item to be replaced.
    """
    max_count = 0
    max_index = -1
    last_zero_index = -1
    count = 0
    for i, x in enumerate(A):
        if x == 1:
            count += 1
        else:
            count = i - last_zero_index
            last_zero_index = i
        if count > max_count:
            max_count = count
            max_index = last_zero_index
    return max_index

if __name__ == '__main__':
    def test_function(f):
        assert f([1,1,1,1]) == -1
        assert f([]) == -1
        assert f([0]) == 0
        assert f([1, 0]) == 1
        assert f([0, 1, 0, 1]) == 2
        assert f([0, 0, 1, 0, 1, 1, 1, 0, 1, 1]) == 7
    test_function(find_index)
    test_function(find_index2)
