'''
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''


# def solution(A):
#     if max(A) < 0:
#         return 1
#
#     A_dic = {x:0 for x in A}
#     sequence_dic = {x: False for x in range(min(A), max(A)+1)}
#
#     for key in A_dic.keys():
#         if key in sequence_dic:
#             sequence_dic[key] = True
#
#     for key, value in sequence_dic.items():
#         if not value:
#             return key
#
#     return max(A)+1

def solution(A):
    seen = [False] * len(A)
    for value in A:
        if 0 < value <= len(A):
            seen[value - 1] = True

    for idx in range(len(seen)):
        if not seen[idx]:
            return idx + 1

    return len(A) + 1


if __name__ == '__main__':
    A = [[1, 3, 6, 4, 1, 2],
         [1, 2, 3],
         [-1, -3]]

    for value in A:
        result = solution(value)
        print(f'Missing number is {result}')



