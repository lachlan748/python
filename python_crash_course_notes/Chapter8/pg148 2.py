def print_models(unprinted, completed):
    # Simulate printing a design until none are left
    while unprinted:
        current = unprinted.pop()

        print(f"Printing model: {current}")
        completed.append(current)

def show_completed_models(completed_models):
    # Show all models that were printed
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)

unprinted = ['tomcat', 'falcon', 'phantom', 'mig']
completed = []

print_models(unprinted[:], completed)
show_completed_models(completed)
