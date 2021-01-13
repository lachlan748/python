number = input("Pick a number and I'll tell you if it's odd or even: ")
number = int(number)

if number % 2 == 0:
	print('The number ' + str(number) + ' is even.')
else:
	print('The number ' + str(number) + ' is odd')
