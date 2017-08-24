"""Given a limited range array of size n where array contains elements between
1 to n-1 with one element repeating, find the duplicate number in it."""

def find_naive(arr):
    """Naive solution using set
    
    Args:
        arr: an array of integers containing single duplicate item.

    Returns:
        Duplicate item.
    """
    seen = set()
    for _, item in enumerate(arr):
        if item in seen:
            return item
        seen.add(item)

def find_using_sum(arr):
    """Sums all elements in the array and subtracts expected sum for without duplicates.

    Args:
        arr: an array of integers containing single duplicate item.

    Returns:
        Duplicate item.
    """
    return sum(arr) - (len(arr) * (len(arr) - 1)) // 2

def find_xor(arr):
    """XOR all elements.

    Args:
        arr: an array of integers containing single duplicate item.

    Returns:
        Duplicate item.
    """
    duplicate = 1
    for i in range(2, len(arr)):
        duplicate ^= i
    for _, item in enumerate(arr):
        duplicate = duplicate ^ item
    return duplicate

if __name__ == '__main__':
    import random

    def test_function(f):
        for _ in range(100):
            n = 10
            arr = [i+1 for i in range(n)]
            duplicate = random.randint(1, n-1)
            arr.append(duplicate)
            random.shuffle(arr)
            assert f(arr) == duplicate

    test_function(find_naive)
    test_function(find_using_sum)
    test_function(find_xor)
