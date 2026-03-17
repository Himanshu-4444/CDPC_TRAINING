# Ways of taking input
n=int(input())  #11
a=int(input())  #11
b=int(input())  #12
a,b=map(int,input().split()) #11 12
a,b,c=map(int,input().split())   #11 12 13
arr=list(map(int,input().split()))  # [11,12,13,14,15]
arr=eval(input())     # [11,12,13,14,15] or {22,33,44,55} or (11,12,13,14,15) or 6*10+2/2*3 it will evaluate the expression and store the result in arr

# Roy and Profile Picture
'''https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/'''

L = int(input())
N = int(input())
W = 0
H = 0
for i in range(N):
                 # Reading input from STDIN
                 W,H=map(int,input().split())
                 if L>W or L>H:
                        print("UPLOAD ANOTHER")
                 elif L<=W and L<=H:
                         if(W==H):
                            print("ACCEPTED")
                         else:
                            print("CROP IT")     # Writing output to STDOUT

# Monk & Rotation
'''https://www.hackerearth.com/problem/algorithm/monk-and-rotation-3-bcf1aefe/'''
""" Question: Rotate an array to the right by a given number of steps 
Input: [1,2,3,4,5] rotated by n=2 steps to the right should become [4,5,1,2,3]"""

T = int(input())
for i in range(T):
    N = int(input())       # Fix 1: input() needs parentheses
    K = int(input())       # Fix 1: input() needs parentheses
    arr = list(map(int, input().split()))  # Fix 2: arr[N] → arr (plain assignment)
    
    K = K % N              # Handle cases where K >= N
    arr1 = arr[N-K:]       # Fix 3: split point is N-K for right rotation
    arr2 = arr[:N-K]
    arr3 = arr1 + arr2
    
    print(*arr3)           # Fix 4: moved inside loop; *arr3 prints space-separated

