#Simple function

def greet_user():
	"""Display a simple greeting."""
	print("Hello!")

greet_user()

# triple quotes above are called Docstrings used to describe what's happening in the function

def greet_user(username):
	"""Display a simple greeting."""
	print("Hello, " + username.title() + "!")

greet_user('lachlan')
greet_user('jane')
greet_user('amber')

# Above, the variable username in the definition of greet_user is the parameter, while the names lachlan, jane and amber are arguments.
# Arguments are passed to the function

def fav_book():
	"""What is your favourite book?"""
	book = "alice in wonderland"
	print("My favourite book is " + book.title() + ".")

fav_book()

def fav_book2(title):
	"""What is your favourite book?"""
	print("My favourite book is " + title.title() + ".")

fav_book2("the road")

# Functions can have multiple parameters and therefore multiple arguments.

# Positional arguments, where the argument order matches the Parameter order.

def people(wife, daughter):
	print("\n" + "My wife's name is " + wife.title() + " and my daughters name is " + daughter.title() + ".")
	print(wife.title() + " makes less noise.")

people("jane", "amber")

#Call the function again with different names.

people("claire", "isabelle")

# Confuse the two:

people("amber", "jane")

# To stop the confusion, use keyword arguments:

people(wife = "jane", daughter = "amber")
people(daughter = "isabelle", wife = "claire")

# Using default values, define them in the parameter:

def describe_pet(pet_name, animal_type = 'dog'):
	print("\n" + "I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name + ".")

describe_pet(pet_name = 'toto')

# Override the default value:

describe_pet(pet_name = 'harry', animal_type = 'hamster')

# Exercise 8-3

def shirt_maker():
	size = 'medium'
	label = 'ansible rocks by red hat'
	print("\n" + "You have ordered shirt size: " + size.title() + ". The printed label will be: " + label.title() + ".")

shirt_maker()

#########

def shirt_maker(size, label):
	print("\n" + "You have ordered shirt size: " + size.title() + ". The printed label will be: " + label.title() + ".")

shirt_maker('small', 'boys rock, girls smell of socks')

#########

# Exercise 8-4:

def shirt_maker(label, size = 'large'):
	print("\n" + "You have ordered shirt size: " + size.title() + ". The printed label will be: " + label.title() + ".")

shirt_maker(label = 'I love python')

# Note: default argument goes last.

# Return values:

def get_formatted_name(first_name, last_name):
	"""Return a neatly formatted name"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print("\n" + musician)


# Optional arguments:

# Move the empty string to the end of the arguments list:

def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a neatly formatted name"""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician1 = get_formatted_name('johnny', 'lee', 'hooker')
print("\n" + musician1)


# Returning a dictionary instead of a string:

def build_person(first_name, last_name):
	"""Return a neatly formatted name"""
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('robert', 'plant')
print()
print(musician)

# Exercise 8-6, pg 146

def city_country(city, country):
	"""Return a city, country pair"""
	location = city + ", " + country
	return location.title()

place = city_country('sydney', 'australia')
print("\n" + place)

# Exercise 8-7, pg 146

def make_album(artist_name, album_name, number_of_tracks=''):
    album_info = {'artist': artist_name, 'name': album_name, 'number': number_of_tracks}
    return album_info

album1 = make_album('daft punk', 'random access memories', '12')
album2 = make_album('peter green', 'then play on')
album3 = make_album('b.b king', 'live at the regal', '14')
print()
print(album1)
print(album2)
print(album3)
