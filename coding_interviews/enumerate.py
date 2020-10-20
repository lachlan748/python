# loop over something and have an automatic counter

fruits = ['apple', 'peach', 'banana', 'strawberry', 'apricot', 'pear']

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# change index starting number to 10

for i, fruit in enumerate(fruits, 10):
    print(f"{i}: {fruit}")

# pair the index and fruit in a list:

fruit_list = list(enumerate(fruits, 1))
print(fruit_list)
