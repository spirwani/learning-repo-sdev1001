#burger dictionary
burger = {
    'patties': 1,
    'patty_type': 'beef',
    'cheese': True,
    'toppings': ['lettuce', 'tomato', 'onion', 'pickles', 'ketchup', 'mustard'],
    'bun': 'sesame seed'
}

#changing values in dictionary
burger['patties'] = 2
burger['patty_type'] = 'vegetarian'
burger['cheese'] = False
burger['bun'] = 'whole wheat'

#getting items
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

#write a value that doesn't exist
burger['gluten_allergy'] = True

gluten_allgery = burger.get('gluten_allergy', False)
if gluten_allgery:
    print("we've removed gluten from burger")