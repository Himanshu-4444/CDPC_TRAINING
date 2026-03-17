no =int(input("Enter a num:"))
rev=0
while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10              #cursor is known as excecution controller 
print("reverse is:",rev)

no=int(input("Enter a number"))
count=0
while no>0:
    no=no//10
    count=count+1
print("No of digits are:",count)

no=int(input("Enter a number"))
sum=0
while no>0:
    rem=no%10
    sum=sum+rem
    no=no//10
print(sum)

# check no is palindrome
no =int(input("Enter a num:"))
no1=no
rev=0
while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10              #cursor is known as excecution controller 
if no1==rev:
    print("palindrome")
else:
    print("not a palindrome")

# check no is armstrong
no=int(input("Enter a number:"))
no1=no
sum=0
count=0
while no>0:
    no=no//10
    count=count+1
no=no1
while no>0:
    rem=no%10
    sum=sum+rem**count
    no=no//10
if no1==sum:
    print("Armstrong")
else:
    print('Not armstrong')

# print armstrong no between 1 to 10000
for HM in range(1,10000):
    no=HM
    no1=no
    sum=0
    count=0
    while no>0:
        no=no//10
        count=count+1
    no=no1
    while no>0:
        rem=no%10
        sum=sum+rem**count
        no=no//10
    if no1==sum:
        print("Armstrong ",HM)


n=int(input("Enter the value of n"))
x=int(input("Enter the value of x"))
sum=1
for i in range(1,n):
    sum=sum+(x**i)/i
print(sum)


# Write a program to check whether a number is even or odd.
# Write a program to find the largest of three numbers.
# Check whether a number is positive, negative, or zero.
# Write a program to check whether a number is divisible by both 3 and 5.
# Write a program to print numbers from 1 to N.
# Write a program to print all even numbers from 1 to N.
# Write a program to calculate the sum of first N natural numbers.
# Write a program to calculate the factorial of a number.
# Write a program to print the multiplication table of a number.
# Write a program to count the number of digits in a number.
# Write a program to reverse a number.
# Write a program to check whether a number is palindrome.
# Write a program to find the sum of digits of a number.
# Write a program to check whether a number is an Armstrong number.
# Write a program to print numbers divisible by 7 between 1 and N.