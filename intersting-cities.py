cities = ['Edmonton', 'Paris', 'Munich', 'Berlin', 'Amsterdam', 'Prague']
cities.pop(0)
print(cities)
city = input('enter city: ')
cities.append(city)
cities.sort()
print(f'list of cities: {cities}')