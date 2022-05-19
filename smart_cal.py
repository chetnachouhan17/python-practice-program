from arithmetic import *
#Single Arithematic operation

def calc():
	ex = input("Enter your expression :")
	def part(x):
		if "+" in x :
			y = x.split("+")
			return y,"+"

		elif "-" in x :
			y = x.split("-")
			return y,"-"

		elif "*" in x :
			y = x.split("*")
			return y,"*"

		elif "/" in x :
			y = x.split("/")
			return y,"/"

		elif "%" in x :
			y = x.split("%")
			return y,"%"

		else : 
			print("Invalid Operation")
			calc()

	def conv(a):
		for i in range(len(a)) : 
			if "." in a[i]:
				a[i] = float(a[i])
			elif a[i] == "": 
				a[i] = 0
			else:
				a[i] = int(a[i])

		return a 

	operand,operator = part(ex)
	operand1 = conv(operand)

	if operator == "+" : 
		result = add(operand1[0],operand1[1])
		result = con(result)
		print(result)

	elif operator == "-" : 
		result = sub(operand1[0],operand1[1])
		result = con(result)
		print(result)

	elif operator == "*" : 
		result = mul(operand1[0],operand1[1])
		result = con(result)
		print(result)

	elif operator == "/" : 
		if operand1[1] == 0 :
			print("Denominator can't be zero")
		else :
			result = div(operand1[0],operand1[1])
			result = con(result)
			print(result)

	elif operator == "%" :
		if operand1[1] == 0:
			print("Denominator can't be Zero") 
		else: 
			result = mod(operand1[0],operand1[1])
			result = con(result)
			print(result)

	else : 
		print("Please enter a valid choice")

def main():
	choice = input("Enter Yes to Continue and No to Close : ")
	if choice == "Yes":
		calc()
		main()

	elif choice == "No":
		exit()

	else : 
		exit()
try : 
	calc()
	main()

except ValueError : 
	print("Enter Valid Value")

except ZeroDivisionError :
	print("Denominator Can't be Zero")

except TypeError : 
	print("Something happened i don't know")

finally :
	print("Thanks for using my calculator")


