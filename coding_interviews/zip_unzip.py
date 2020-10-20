# zip combines two lists

first_names = ['john', 'paul', 'george', 'ringo']

last_names = ['lennon', 'mccartney', 'harrison', 'starr']

for first_name, last_name in zip(first_names, last_names):
    print(f"{first_name.title()} {last_name.title()}")

# add a third list

ages = ['40', '78', '58', '80']

for first_name, last_name, age in zip(first_names, last_names, ages):
    print(f"{first_name.title()} {last_name.title()}, age: {age}")


# alternatively, print them as a list:

beatles_list = list(zip(first_names, last_names, ages))
print(beatles_list)

for i in beatles_list:
    print(i)

# unzip a list using zip*

first_name, last_name, age = list(zip(*beatles_list))
print(f"Unzipped list: {first_name} {last_name}, age: {age}")
