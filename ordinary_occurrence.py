'''
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.

'''


def solution(A):
    # write your code in Python 3.6
    # odd = [x for x in A if A.count(x) % 2 == 1]
    # print(odd[0])
    # return odd[0]

    print(A)


    while 0 < len(A):
        for i in range(len(A)):
            idx = []
            count = 0
            for j in range(len(A)):
                print(f'Aj: {A[j]}, Ai:{A[i]}')
                if A[j] == A[i]:
                    count += 1
                    idx.append(j)
            print(f'count={count}, idx={idx}')

            if count % 2 == 0:
                del A[idx]
                print(f'new A = {A}')
                break
            else:
                return A[idx[0]]







            if A.count(A[i])%2 == 0:
                del A[i]
            else:
                return A[i]


if __name__ == '__main__':

    # aa = {'a': 1, 'b':2, 'c':3}
    # a, *b = aa.values()
    # # print(f'{a}, {b}, {c}')
    # print(f'{a}, {b}')

    A = [9, 3, 9, 3, 9, 7, 9]
    result = solution(A)
    print(f'In {A}, the odd number is {result}')
