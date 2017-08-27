"""Given an array of integers, find largest sub-array formed by consecutive integers.
The sub-array should contain all distinct values."""

def max_consecutive(A):
    positions = dict()
    ans = (0, 1)

    for start in range(len(A)):

        min_val = A[start]
        max_val = A[start]

        for i in range(start, len(A)):

            consicutive = max_val - min_val + 1 == i - start
            better = (i - start) >= ans[1] - ans[0]
            if consicutive and better:
                ans = (start, i)

            if positions.get(A[i], -1) >= start and start != i:
                break

            positions[A[i]] = i
            if A[i] < min_val:
                min_val = A[i]
            if A[i] > max_val:
                max_val = A[i]

    return A[ans[0]:ans[1]]

if __name__ == '__main__':
    assert max_consecutive([2, 0, 2, 1, 4, 3, 1, 0]) == [0, 2, 1, 4, 3], max_consecutive([2, 0, 2, 1, 4, 3, 1, 0])
