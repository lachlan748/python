# sets remove duplicates from lists

interfaces = ['eth1', 'eth2', 'eth2', 'eth26', 'eth21', 'eth1']

cleaned_interfaces = set(interfaces)
print(cleaned_interfaces)

# now fix order

ordered_interfaces = sorted(cleaned_interfaces)
print(ordered_interfaces)

# use a list comprehension and set

interfaces = ['1', '2', '2', '26', '21', '1']

find_duplicates = set([x for x in interfaces if interfaces.count(x) > 1])
print(find_duplicates)

# use intesection to find common items in two sets:

first_interfaces = set(['eth1', 'eth2', 'eth2', 'eth26', 'eth21', 'eth1'])
second_interfaces = set(['eth47', 'eth3', 'eth2', 'eth26', 'eth11', 'eth17'])

common_interfaces = first_interfaces.intersection(second_interfaces)
print(common_interfaces)

# find items that only exist in 2nd set but not in 1st set

uncommon_interfaces = first_interfaces.difference(second_interfaces)
print(uncommon_interfaces)
