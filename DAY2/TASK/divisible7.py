# Write a program to print numbers divisible by 7 between 1 and N.
N=int(input("Enter the value of N: "))
for i in range(1, N+1):
    if i%7==0:
        print(i)