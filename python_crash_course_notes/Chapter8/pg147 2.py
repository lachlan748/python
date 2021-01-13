def my_greeting(names):
    # Print a simple greeting message to each user
    for name in names:
        msg = f"Hello {name.title()}!"
        print(msg)

usernames = ['john', 'paul', 'george', 'ringo']
my_greeting(usernames)
