"""Given two sorted arrays X[] and Y[] of size m and n each, merge elements of X[] with
elements of array Y[] by maintaining the sorted order. i.e. fill X[] with first
m smalles elements and fill Y[] with remaining elements."""

def inplace_merge(X, Y):
    """O(N*M) solution where N = length(X) and M = length(Y).

    Args:
        X: An sorted array of integers.
        Y: An sorted array of integers.
    """
    for i in range(len(X)):
        if X[i] > Y[0]:
            X[i], Y[0] = Y[0], X[i]
            _sift_up(Y)


def _sift_up(Y):
    i = 0
    while i + 1 < len(Y) and Y[i] > Y[i + 1]:
        Y[i], Y[i + 1] = Y[i + 1], Y[i]
        i += 1

if __name__ == '__main__':
    import random
    n = 100
    for __ in range(1000):
        X = sorted([random.randint(-10, 10) for _ in range(n)])
        Y = sorted([random.randint(-10, 10) for _ in range(n)])
        sorted_together = sorted(X + Y)
        inplace_merge(X, Y)
        assert X == sorted_together[:n] and Y == sorted_together[n:]
