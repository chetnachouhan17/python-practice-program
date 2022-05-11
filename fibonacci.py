n=int(input("enter the number to print fibonacii series : "))
n1=0
n2=1
count=0

if n<=0:
        print("please enter a positive integer")
elif n == 1:
        print("Fibonacci series upto", n ,":")
        print(n1)
else:
    print("fibonacci series:")
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
