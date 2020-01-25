number = input("Give me a number and I'll check if it's divisible by 10: ")
number = int(number)

if number % 10 == 0:
	print("\nYes, " + str(number) + " can be divided by 10.")
else: 
	print("\nNo, " + str(number) + " cannot be divided by 10 evenly.")
