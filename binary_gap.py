# 1. BinaryGap
# Find longest sequence of zeros in binary representation of an integer.

"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.
Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..2,147,483,647].
"""

import numpy as np


def solution(N):
    # write your code in Python 3.6
    N_bin = bin(N).replace('0b', '')
    # print(N_bin)

    current_count = 0
    best_count = 0
    for i in range(len(N_bin)):
        checkpoint = N_bin[i]
        if checkpoint == '1':
            if current_count > best_count:
                best_count = current_count
            current_count = 0
        elif checkpoint == '0':
            current_count += 1
        # print(f'{i}: {current_count}')

    return best_count


if __name__ == '__main__':
    # 561892, 74901729, 1376796946
    np.random.seed(77)
    N = np.random.randint(1, 1376796946)
    N = 561892
    zero_count = solution(N)
    print(f'{N}: {bin(N)}: {zero_count}')


