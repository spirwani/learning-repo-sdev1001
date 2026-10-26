#burger dictionary
burger = {
    'patties': 1,
    'patty_type': 'beef',
    'cheese': True,
    'toppings': ['lettuce', 'tomato', 'onion', 'pickles', 'ketchup', 'mustard'],
    'bun': 'sesame seed'
}

print("Here's what's in the burger: ")
print(f"{burger['patties']} {burger['patty_type']} patties is on your burger")

print(f"Your burger has {burger['bun']} bun.")
if burger['cheese']:
    print("cheese is on your burger")
else:
    print("no cheese is on your burger")

print("Here's a toppings list: ")
for topping in burger['toppings']:
    print(f"-{topping}")