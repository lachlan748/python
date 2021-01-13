def make_my_sandwich(bread_type, *ingredients):
    # Print a list of ingredients to make the perfect sandwich
    print(f"\nMaking a sandwich with the following ingredients on {bread_type} bread: ")
    for item in ingredients:
       print(f"- {item}")
