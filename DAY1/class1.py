no=int(input("enter a number:"))
res=no%10
print(res)

no=int(input("enter number:"))#sum of 2 digit number
n1=no%10
n2=no//10
res=n1+n2
print(res)

num=int(input("Enter num: ")) #sum of 3 digit number
n1=num%10
num=num//10
n2=num%10
num=num//10
n3=num%10
res=n1+n2+n3
print(res)

num=int(input("Enter num: "))#sum of 6 digit number
n1=num%10
num=num//10
n2=num%10
num=num//10
n3=num%10
num=num//10
n4=num%10
num=num//10
n5=num%10
num=num//10
n6=num%10
res=n1+n2+n3+n4+n5+n6
print(res)

num=int(input("Enter num: "))#sum of 6 digit number
n1=num%10
num=num//10
n2=num%10
num=num//10
n3=num%10
num=num//10
n4=num%10
num=num//10
n5=num%10
num=num//10
n6=num%10
res=n1,n2,n3,n4,n5,n6
res1=n1*100000+n2*10000+n3*1000+n4*100+n5*10+n6
print(res)
print(res1)

num=int(input("Enter num: "))#sum of 1st and 9th digit
n1=num%10
n2=num//100000000
n3=num//(10**8)
res=n1+n2
print(res)
print(n3+n1)

#accept basic salary and calculate gross salary
basic=float(input("Enter basic salary:"))
salary=basic+basic*0.2+basic*0.3+basic*0.4
print("Gross salary is:",salary)

# Write a program to calculate the perimeter of a rectangle using length and width entered by the user.

# Write a program to convert kilometers into meters and centimeters.

# Write a program to calculate the total bill amount if a user buys 3 products (take price of each product as input).

# Write a program to convert hours into minutes and seconds.

# Write a program to calculate the total number of seconds in a given number of days.

# Write a program to convert rupees into paise.

