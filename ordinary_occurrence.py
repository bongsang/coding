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


'''
package com.codility.lesson02.arrays;

import java.util.HashMap;
import java.util.Set;

public class OddOccurrencesInArray {
  public int solution(int[] A) {
    HashMap <Integer, Integer> occurrencesMap = new HashMap<Integer, Integer>();
    
    for(int i=0; i<A.length; i++) {
      if(occurrencesMap.containsKey(A[i])) {
        int occurrences = occurrencesMap.get(A[i]);
        occurrences++;
        occurrencesMap.put(A[i], occurrences); //increment occurrence counter and store it
      }
      else {
        occurrencesMap.put(A[i], 1); //1st occurrences of this value
      }
    }

    Set keySet = occurrencesMap.keySet();
    
    for(int currentKey : keySet) {
      int occurrences = occurrencesMap.get(currentKey);
      
      //if occurs odd number of times, we found the unpaired value - no need to continue checking
      if(occurrences % 2 != 0) return currentKey;
    }
    //should never get to here
    throw new RuntimeException("shouldn't get to here - should've return unpaired value by now");
  }
}
'''


def solution(A):
    dic = { x:0 for x in A }

    for i in range(len(A)):
        if A[i] in dic:
            dic[A[i]] += 1

    for key, value in dic.items():
        if value % 2 == 1:
            return key


if __name__ == '__main__':
    A = [9, 3, 9, 3, 9, 7, 9]

    result = solution(A)
    print(f'In {A}, the odd number is {result}')
