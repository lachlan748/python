def make_my_sandwich(*ingredients):
    # Print a list of ingredients to make the perfect sandwich
    print("\nMaking a sandwich with the following ingredients: ")
    # print(type(ingredients))
    for item in ingredients:
       print(f"- {item}")

make_my_sandwich('cheese')
make_my_sandwich('cheese', 'ham')
make_my_sandwich('cheese', 'tuna', 'sweetcorn')
