def add():
    res=a+b
    return res

if __name__=="__main__":
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    res=add()
    print(res)

def add(x,y):
    res=x+y
    return res

if __name__=="__main__":
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    res=add(a,b)
    print(res)

def is_leap(year):
    leap = False
    
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                leap=True
            else:
                leap=False
    else:
        leap=False
    return leap

year = int(input())

#Task are done on hackerrank.