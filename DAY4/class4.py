# Solve Me First

def solveMeFirst(a,b):
	# Hint: Type return a+b below
    return(a+b)


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)


Complete the  function with the following parameter(s):
ar[n]: an array of integers



# Complete the 'simpleArraySum' function below.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    sum=0
    for i in ar:
        sum+=i
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

#List
ls=[11,22,33,44,55,66,77,88,99]
print(ls)
for i in range(len(ls)):
    print(ls[i])
for x in ls:
    print(x)

#List Slicing
#
ls=[11,22,33,44,55,66,77,88,99,100]
print(ls[0])
print(ls[5])
print(ls[-1])
print(ls[-2])
print(ls[2:5])
print(ls[3:7])
print(ls[:5])
print(ls[4:])
print(ls[:])
print(ls[::1])
print(ls[::2])
print(ls[::-2])

#Accept 4 numbers and print max and min 
n1=int(input("Enter the number:"))
n2=int(input("Enter the number:"))
n3=int(input("Enter the number:"))
n4=int(input("Enter the number:"))
max=n1
if max<n2:
    max=n2
if max<n3:
    max=n3
if max<n4:
    max=n4
print("The maxx number is: ",max)


for i in range(4):
    num=int(input("Enter a " + str(i+1) + " number: "))
    if i==0:
        max=num
        min=num
    else:
        if num>max:
            max=num
        if num<min:
            min=num
print("Max:", max)
print("Min:", min)