#Looping thru lists

bikes = ['ducati', 'yamaha', 'suzuki', 'honda', 'aprilia']
for bike in bikes:
#	print(bikes)
	print(bike.title() + ' is a good bike to ride.')
	print("I can't wait to own a " + bike.title() + "." + '\n')

#Add an action outside the loop by removing the indent:

print('That was a great list that I looped through.')

##### Exercise, pg 60.

pizzas = ['four cheese', 'hawaiian', 'pepperoni', 'meat lovers', 'marinara']
for pizza in pizzas:
	print('I love ' + pizza.title() + " pizza." + '\n')

print("In actual fact, I love all kinds of pizza.")

#### Working with numerical lists using the 'range' function.

print('\n')
for value in range(1,5):
	print(value)

#Note that python starts counting at the first value you give it, 1, not 0.

for value in range(1,6):
	print(value)

#Convert a range of numbers into a list by wrapping list around the range function:

numbers = list(range(1,6))
print(numbers)

### Skip items in a range:

#Below, we start at 2 then add 2 until it passes the end value, 11. 

even_numbers = list(range(2,11,2))
print(even_numbers)

# Now make a list of the first 10 squared numbers:

squares = []
for value in range(1,21):
	square = value**2
	squares.append(square)

print(squares)

#To make the code neater, remove the temporary variable 'square' and append each value to the list:

squares = []
for value in range(1,21):
	squares.append(value**2)

print(squares)

###### Simple statistics:

digits = [1,2,3,4,5,6,7,8,9,0]
msg_a = min(digits)
msg_b = max(digits)
msg_c = sum(digits)
print(msg_a)
print(msg_b)
print(msg_c)

###### List comprehensions:

#Combines lines of code into one eg. finding the squares of numbers.

squares = [value**2 for value in range(1,11)]
print(squares)

power_of_3 = [value**3 for value in range(1,11)]
print(power_of_3)

####### Working with part of a list, known as a slice:

#Specify the index of the first and last elements you want to work with.

players = ['lachlan', 'tony', 'saty', 'nilesh', 'peter']
print(players[0:3])
print(players[2:4])

#Omit the first index, python starts at the beginning:

print(players[:5])

#Start the end of a list:

print(players[3:])

#Negative index is chosen from the end of a list:

print(players[-4:])

#Looping through a slice:

print('\nHere are the members of my team:')
for x in players[:4]:
	print(x.title())

### Copying a list:

#Often, you'll start with an existing list and make an entirely new list based on the old one.

#To copy a list, make a slice and omit the first and second index ([:])

my_foods = ['pizza', 'falafel', 'chocolate cake']
friend_foods = my_foods[:]

my_foods.append('spaghetti')
friend_foods.append('ice cream')

print('\nMy favourite foods are:')
print(my_foods)

print('\nMy friends favourite foods are:')
print(friend_foods)

###############

### Exercise pg. 69

my_pizza = ['supreme', 'bbq chicken', 'vegetarian', 'hawaiian']
my_friends_pizza = my_pizza[:]
print('\n\n\nMy new pizza list is:')
print(my_pizza)
print('\nMy friends pizza list is:')
print(my_friends_pizza)
# Now update both:
my_pizza.append('four cheese')
my_friends_pizza.append('pepperoni')
print('\nMy new updated pizza list is:')
print(my_pizza)
print('\nMy friends updated pizza list is:')
print(my_friends_pizza)

####################

#### Tuples - create a list of items that cannot change. Tuples includes items that are 'immutable'. An immutable list is called a 'tuple'.

#Define a tuple. List a list but use parenthesis instead of square brackets.

dimensions = (200,50)
print('\n')
print(dimensions[0])