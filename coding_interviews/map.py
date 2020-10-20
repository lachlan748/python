# applies a function to items in a list

# old school way

numbers = [100, 20, 10, 5, 4, 3, 2, 1]
results = []

# multiply each number by 3, append to results list

for i in numbers:
    results.append(i*3)

print(results)

# now use map to simplify:

results = list(map(lambda x: x*3, numbers))

print(f"Results with map: {results}")
