# def cyclic(idx, length, shift):
#     position = idx + shift
#     if position >= length:
#         position = position - length
#
#     return position
#

def solution(A, K):
    # write your code in Python 3.6
    B = A[:]
    for i in range(len(A)):
        B[(i+K)%len(A)] = A[i]

    return B


if __name__ == '__main__':
    A = [3, 8, 9, 7, 6]
    B = solution(A, 3)
    print(f'{A} --> {B}')

