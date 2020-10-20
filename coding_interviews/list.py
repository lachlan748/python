# list() constructor returns a python list

vowels = 'aeiou'
print(list(vowels))

vowels_tuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowels_tuple))

interfaces = {'eth1': 'server1',
              'eth2': 'server2',
              'eth3': 'server3',
              'eth4': 'server4'}

# create a list from dict keys
print(list(interfaces))
