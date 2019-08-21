'''
A non-empty zero-indexed array A consisting of N integers is given.
A pair of indices (P, Q), where 0 ≤ P < Q < N, is said to have adjacent values if no value
in the array lies strictly between values A[P] and A[Q].
For example, in array A such that:
A[0] = 0 A[1] = 3 A[2] = 3
A[3] = 7 A[4] = 5 A[5] = 3
A[6] = 11 A[7] = 1
the following pairs of indices have adjacent values:
(0, 7), (1, 2), (1, 4),
(1, 5), (1, 7), (2, 4),
(2, 5), (2, 7), (3, 4),
(3, 6), (4, 5), (5, 7).
For example, indices 4 and 5 have adjacent values because there is no value in array A that lies
strictly between A[4] = 5 and A[5] = 3; the only such value could be the number 4,
and it is not present in the array.
Write a function that returns number of adjacent values
'''


def solution(A):
    if len(A) == 1:
        return -2
    else:
        A.sort()
        # print(f'sorted A = {A}')

    distance_min = 0
    for i in range(1, len(A)):
        distance_current = A[i] - A[i - 1]
        # print(f'{A[i]} - {A[i-1]} = {distance_current}')
        if distance_current < distance_min:
            distance_min = distance_current

    # print(f'distance minimum = {distance_min}')
    if distance_min > 100000000:
        return -1
    else:
        return distance_min


if __name__ == '__main__':
    A = [[0, 3, 3, 7, 5, 3, 11, 1],
         [1, 5, 8, 13]]

    for value in A:
        result = solution(value)
        print(f'minimum distant is {result}')
