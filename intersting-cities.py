cities = ['Edmonton', 'Paris', 'Munich', 'Berlin', 'Amsterdam', 'Prague']
cities.pop(0)
print(cities)
city = input('enter city: ')
cities.append(city)
cities.sort()
print(f'list of cities: {cities}')
invalid_city = ['Munich', 'Berlin']
for city in cities:
    if city in invalid_city:
        print(f"{city} is not an interesting place to visit")
    else:
        print(f"{city} is an interesting place to visit")
