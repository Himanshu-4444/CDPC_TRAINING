#Comapre the Triplets
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice=0
    bob=0
    for i in range(len(a)):
        if(a[i]>b[i]):
            alice+=1
        elif(a[i]==b[i]):
            pass
        else:
            bob+=1
    return (alice,bob)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



#Diagonal Difference
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sumL=0
    sumR=0
    diff=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i==j):
                sumL+=arr[i][j]
            if(i+j==len(arr)-1):
                sumR+=arr[i][j]
            else:
                pass
    diff=sumL-sumR
    return(abs(diff))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#Plus Minus

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos=0
    neg=0
    zer=0
    for i in range(len(arr)):
        if(arr[i]>0):
            pos+=1
        elif(arr[i]<0):
            neg+=1
        else:
            zer+=1
    print (f"{pos/n:.6f}")
    print (f"{neg/n:.6f}")
    print (f"{zer/n:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

#A Very Big Sum

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    sum=0
    for i in range(len(ar)):
        sum=sum+ar[i]
    return(sum)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

'''https://www.hackerrank.com/challenges/compare-the-triplets/problem

https://www.hackerrank.com/challenges/a-very-big-sum/problem

https://www.hackerrank.com/challenges/diagonal-difference/problem

https://www.hackerrank.com/challenges/plus-minus/problem'''
