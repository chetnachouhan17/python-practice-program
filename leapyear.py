#write a program whether the year is leap or not

a=int(input("enter year"))

if(a%400==0):
    print("a is a leap year")
elif(a%100==0):
   print("a is not a leap year")
elif(a%4==0):
   print("a is a leap year")
else:
 print("not a leap year")
