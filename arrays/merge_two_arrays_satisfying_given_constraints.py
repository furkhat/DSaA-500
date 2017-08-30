"""Given two sorted arrays X[] and Y[] of size m and n each where m >= n and
X has exactly n vacant cells, merge lements of Y[] in their correct position
in array X[] i.e merge (X, Y) by keeping the sorted order.
The vacant cells in X[] is represented by 0
"""

def merge_naive(X, Y):
    """Merges Y to X by first filling Y to the vacant cells and sorting. O(nlogn).

    Args:
        X: An array of integers in sorted order except vacant 0 elements.
        Y: A sorted array of numbers of size equal to the number of vacant cells in X.
    """
    j = 0
    for i in range(len(X)):
        if X[i] == 0:
            X[i] = Y[j]
            j += 1

    X.sort()

def merge_linear(X, Y):
    """Merges Y to X in O(m + n) time by first moving all elements in X to the end and
    applying merge similar to in merge sort.

    Args:
        X: An array of integers in sorted order except vacant 0 elements.
        Y: A sorted array of numbers of size equal to the number of vacant cells in X.
    """
    izerro = len(X) - 1
    for i in range(len(X) - 1, -1, -1):
        if X[i] is not 0:
            X[i], X[izerro] = X[izerro], X[i]
            izerro -= 1

    i = len(Y)
    j = 0
    k = 0
    while j < len(Y):
        if i < len(X) and X[i] < Y[j]:
            X[k] = X[i]
            X[i] = 0
            k += 1
            i += 1
        else:
            X[k] = Y[j]
            k += 1
            j += 1

if __name__ == '__main__':
    import random
    m = 100 
    for __ in range(1000):
        n = random.randint(0, m)
        x = sorted([random.randint(1, 1000) for _ in range(m-n)])
        X = [0] * m
        j = 0
        for i in range(len(X)):
            if j == len(x):
                break
            if len(X) - i == len(x) - j:
                X[i] = x[j]
                j += 1
            else:
                if random.randint(0, 1):
                    X[i] = x[j]
                    j += 1
        assert X.count(0) == n
        Y = sorted([random.randint(1, 1000) for _ in range(n)])
        X_naive = X
        X_linear = [item for item in X]
        merge_naive(X_naive, Y)
        merge_linear(X_linear, Y)
        assert X_naive == X_linear
