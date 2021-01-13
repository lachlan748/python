alien_0 = {'colour': 'green', 'points': '5'}
print(alien_0['colour'])
print(alien_0['points'])

#Dictionaries are a collection of 'key-value pairs'.

#To pull the code from above:

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Adding information to a dictionary:

print("\n")
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Now the dictionary contains 4x key-value pairs.

#Start with an empty dictionary:

alien_1 = {}
print(alien_1)

alien_1['colour'] = 'blue'
alien_1['points'] = 10

print(alien_1)

#Changing the value of a key-value pair:

print("The colour of alien_1 is " + alien_1['colour'] + ".")

alien_1['colour'] = 'yellow'

print("Now the colour of alien_1 is " + alien_1['colour'] + ".")

#More interesting:

alien_0 = {'colour': 'green', 'points': '5', 'x_pos': '0', 'y_pos': '25', 'speed': 'medium'}
print("Original x-position is " + str(alien_0['x_pos']))

#Move alien to the right

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_pos'] = int(alien_0['x_pos']) + x_increment

print("New x-position: " + str(alien_0['x_pos']))

# Removing key-value pairs permanently using the del statement.

print()
print(alien_0)
del alien_0['points']
print(alien_0)

#A dictionary of similar objects:

fav_languages = {
	'lachlan': 'python',
	'jane': 'javascript',
	'amber': 'scratch',
	}

print()
print(fav_languages)
print()
print("Jane's favourite language is " + fav_languages['jane'].title() + ". Woohoo, what a rockstar!")
print()
print(fav_languages['jane'].title())
print()
print("Jane's favourite language is repeatedly " +
	fav_languages['jane'].title() + ".")


# Exercise pg. 102

print()

jane = {
	'firstname': 'jane',
	'surname': 'smith',
	'age': '48',
	'sex': 'female'
	}

print(jane)

#Looping thru a dictionary:

user_0 = {
		'firstname': 'jane',
	'surname': 'smith',
	'age': '48',
	'sex': 'female'
	}

print("\n" + str(user_0))

for key, value in user_0.items():
	print("\nKey:" + key)
	print("Value: " + value)

# change variable name:

for x, y in user_0.items():
	print("\nKey:" + x)
	print("Value: " + y)

# Loop thru languages:

for x, y in fav_languages.items():
	print(x.title() + "'s favourite language is:")
	print(y.title())

# Use the keys() method instead of items():

for x in fav_languages.keys():
	print("\n" + x.title())

friends = ['jane', 'amber']

for name in fav_languages.keys():
	print("\n" + name.title())

	if name in friends:
	 	print("Hi " + name.title() +
	 		", I see your favourite language is " +
	 		fav_languages[name].title() + "!")

#See if a key exists:

if 'erin' not in fav_languages:
	print("\nErin, please take our poll!")

#Sort key-value pairs in a dict using sort:

for name in sorted(fav_languages.keys()):
	print("\n" + name.title() + ", thankyou for taking the poll.")

#View values without keys using values method:

print()
print("The following languages have been mentioned: ")
for language in fav_languages.values():
	print(language.title())

#What about repeats in a dictionary?

print()
fav_languages = {
	'lachlan': 'python',
	'jane': 'python',
	'amber': 'scratch'
	}

print("The following languages have been mentioned: ")
for language in set(fav_languages.values()):
	print(language.title())

#Exercise pg. 108:

glossary = {
	'mutable': 'a variable that can be changed',
	'immutable': 'a variable that cannot be changed',
	'key': 'a name given to items listed in a dictionary',
	'value': 'a named unit assocated with a key within a dictionary',
	'method': 'a built in way of sorting data within a dictionary',
    }

for x, y in glossary.items():
	print("In programming, a " + x.title() + " is " + y)

##########

rivers = {
	'australia': 'macquarie',
	'egypt': 'nile',
	'england': 'thames',
	'france': 'seine',
	'scotland': 'tay',
    }

print()
print(rivers)

for country, river in rivers.items():
	print("The river " + river.title() + " runs through " + country.title() + ".")

print()

print("The rivers in this data set include:")
for country, river in rivers.items():
    print("- " + river.title())

print()
print("The countries in this data set include:")
for country, river in rivers.items():
    print("- " + country.title())

# Nested dictionaries - expand the alien dictionary to include many aliens

print()

alien_0 = {'colour': 'green', 'points': '5'}
alien_1 = {'colour': 'blue', 'points': '10'}
alien_2 = {'colour': 'red', 'points': '15'}
alien_3 = {'colour': 'purple', 'points': '20'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

# Create a fleet of 30 aliens:

print()

aliens = []

for alien_number in range(30):
	new_alien = {'colour': 'green', 'points': '5', 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print("...")

#Show how many total aliens have been printed:

print("The total amount of aliens created is " + str(len(aliens)))

# Amend the alien characteristics: first 3x aliens to yellow, medium speed and 10 points:

print()

aliens = []

for alien_number in range(30):
	new_alien = {'colour': 'green', 'points': '5', 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['colour'] == 'green':
		alien['colour'] = 'yellow'
		alien['points'] = '15'
		alien['speed'] = 'medium'
	elif alien['colour'] == 'yellow':
		alien['colour'] = 'orange'
		alien['points'] = '25'
		alien['speed'] = 'fast'


for alien in aliens[:10]:
	print(alien)
print("...")

# Lists inside a dictionary:

print()
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'ham', 'anchovies'],
	}

print("You have ordered a " + pizza['crust'] + " crusted pizza " +
	"with the following toppings:")

for x in pizza['toppings']:
	print("\t" + x)

# More lists inside dictionaries:

fav2_languages = {
	'lachlan': ['python', 'c sharp'],
	'jane': ['javascript', 'ruby'],
	'amber': ['scatch', 'html'],
	}

for x, y in fav2_languages.items():
	print("\n" + x.title() + "'s favourite languages are: ")
	for language in y:
		#print("\t" + str(y).title())
		print("\t- " + str(y).title())

# Dictionary in a dictionary:

print()
users = {
	'lfalconer': {
	    'first': 'lachlan',
	    'last': 'falconer',
	    'born': 'sydney',
	    },
	'ssmith': {
	    'first': 'amber',
	    'last': 'falconer',
	    'born': 'london',	
	    }
    }

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['born']

	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())

# Exercise pg. 114

print()
people = {
	'lfalconer': {
	    'first': 'lachlan',
	    'last': 'falconer',
	    'born': 'sydney',
	    'age': '40',
	    'sex': 'male',
	    },
	'afalconer': {
	    'first': 'amber',
	    'last': 'falconer',
	    'born': 'london',
	    'age': '8',
	    'sex': 'female',
	    },
	'jsmith': {
	    'first': 'jane',
	    'last': 'smith',
	    'born': 'beckenham',
	    'age': '48',
	    'sex': 'female',	
	 	}
    }

for username, user_info in people.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['born']
	age = user_info['age']
	sex = user_info['sex']

	print(full_name.title() + " is a " + sex + " and is " + age + " years old.")
