num=int(input("enter a no to find it is prime or not"))
i=2
while(i<=num-1):
    if(num%i==0):
        print("it is not a prime no.")
        break
    else:
        print("it is a prime no.")
        break
else:
        print("no it is not a prime no.")
        
