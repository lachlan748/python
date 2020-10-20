# creates a list of elements for which a function returns true

# print numbers that are greater than zero

my_numbers = [5, 3, 1, 0, -2, -4, -6]

greater_than_zero = list(filter(lambda x: x > 0, my_numbers))
print(greater_than_zero)


# without lambda

def return_squared(num):
    """ squares a number then checks if it's divisble by 2 """

    result = num**2
    if result % 2 == 0:
        return True
    else:
        return False

numbers_divisible_by_two = list(filter(return_squared, my_numbers))
print(numbers_divisible_by_two)
