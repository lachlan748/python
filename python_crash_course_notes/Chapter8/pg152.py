def make_my_sandwich(bread_type, *ingredients):
    # Print a list of ingredients to make the perfect sandwich
    print(f"\nMaking a sandwich with the following ingredients on {bread_type} bread: ")
    # print(type(ingredients))
    for item in ingredients:
       print(f"- {item}")

make_my_sandwich('white', 'cheese')
make_my_sandwich('rye', 'cheese', 'ham')
make_my_sandwich('sourdough', 'cheese', 'tuna', 'sweetcorn')
