cars = ['bmw', 'toyota', 'ford', 'honda', 'ferrari']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

###########

#Equality Operator:

#Lachlans-MBP-15:mono-network lachlanfalconer$ python
#Python 2.7.14 (default, Mar 22 2018, 14:43:05) 
#[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
#Type "help", "copyright", "credits" or "license" for more information.
#>>> car = 'bmw' 
#>>> car == 'bmw'
#True
#>>> car = 'audi'
#>>> car == 'bmw'
#False

#Above is case sensitive.

#############

requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print('Hold the anchovies')

#>>> age = 40
#>>> age > 21
#True
#>>> age < 21
#False
#>>> age == 40
#True

#############

#Check if a value is in a list

toppings = ['tomato', 'salt', 'anchovies', 'peppers']
favourite_toppings = 'ham'
if favourite_toppings not in toppings:
	print(favourite_toppings.title() + " needs to be added to my pizza!")

############

#Simple if statements

age = 19
if age >= 18:
	print("You are old enough to vote")
	print("Have you registered to vote yet?")

#Modify to include else:

age = 17
if age >= 18:
	print("You are old enough to vote")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you're too young to vote")

#The if-elif-else chain

age = 2
if age < 4:
	print("Admission cost is free")
elif age < 18:
	print("Admission cost is £5")
else:
	print("Admission cost is £10")

# Swap for variables

age = 19
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10

print("The price for admission is £" + str(price) + ".")

#Use many elif statements:

age = 70
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age <= 40:
	price = 10
elif age > 65:
	price = 5

print("The price for admission is £" + str(price) + ".")

# The above if-elif-else statments are useful when you want to pass only one test.

#Test multiple conditions

requested_toppings = ['ham', 'mushrooms', 'olives']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'peppers' in requested_toppings:
	print("Adding peppers.")
if 'olives' in requested_toppings:
	print("Adding olives.")

print("Finished making your pizza.")

# Exercise page 89

age = 65

if age < 2:
	print("You are still a baby")
elif age >= 2 and age < 4:
	print("You are a toddler")
elif age >= 4 and age < 13:
	print("You are a kid")
elif age >= 13 and age < 20:
	print("You are a teenager")
elif age >= 20 and age < 65:
	print("You are an adult")
else:
	print("You are an pensioner")

#Efficient loop code:

requested_toppings = ['ham', 'mushrooms', 'olives']

for x in requested_toppings:
	print("Adding " + x + ".")

print("Finshed making your pizza")

#Adding an if


requested_toppings = ['ham', 'mushrooms', 'olives', 'peppers']

for x in requested_toppings:
    if x == 'peppers':
    	print("Sorry, we're out of peppers")
    else:
	    print("Adding " + x + ".")

print("Finshed making your pizza")

#Check the list is not empty:

requested_toppings = []

if requested_toppings:
	for x in requested_toppings:
		print("Adding " + x + ".")
	print("\nFinished making your pizza!")

else:
	print("Are you sure you want a plain pizza?")

# Multiple lists:

print()

available_toppings = ['ham', 'mushrooms', 'olives', 'anchovies', 'peppers']

requested_toppings = ['fries', 'asparagus', 'bbq sauce', 'ham', 'peppers']

for x in requested_toppings:
	if x in available_toppings:
		print("Adding " + x + " to your pizza.")
	else:
		print("Sorry, we don't have " + x + ".")

print("Finished making your pizza")

print()
print()

############

#Exercise pg.93

current_users = ['lachlan', 'ben', 'brad', 'mark', 'victor', 'andrew', 'ajaib']

new_users = ['saty', 'tony', 'nilesh', 'peter', 'davinder', 'victor', 'ANDREW']

for user in new_users:
	if user.lower() in current_users:
		print("I'm sorry " + str(user.title()) + " that username is taken. Please choose a new username.")
	else:
		print("Hi " + str(user.title()) + "! That username is available. Welcome :)")

############

print()

my_numbers = [1,2,3,4,5,6,7,9]

for number in my_numbers:
	if number == 1:
		print(str(number) + "st")
	elif number == 2:
		print(str(number) + "nd")
	elif number == 3:
		print(str(number) + "rd")
	else:
		print(str(number) + "th")

