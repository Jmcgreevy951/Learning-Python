# 4.3

for value in range(1, 101):
   print(value)

# 4.5
numbers = [value for value in range(1, 1000001)]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4.6
odds = [value for value in range(1, 21, 2)]

print(odds)

# 4.7
threes = [value*3 for value in range(1, 11)]

print(threes)

# 4.8
cubes = [value**3 for value in range(1, 11)]

print(cubes)

# 4.9
cubes = []

for value in range(1, 11):
    value = value**3
    cubes.append(value)
    print(value)

print(cubes)


# 4.10
countries = ['Switzerland', 'Australia', 'China', 'America', 'Portugal']

print(f"Three items at the end of the list are:")
for country in countries[2:]:
    print(country.title())

# 4.11
pizzas = ['Ham', 'Chicken', 'Mushroom', 'Peppers']
friend_pizzas = pizzas[:]
other_pizzas = pizzas[:]

pizzas.append('Pork')
friend_pizzas.append('Beef')

del other_pizzas[0]
del other_pizzas[2]

other_pizzas.append('Ice')
other_pizzas.append('Grass')

print("My favourite pizzas are:")
for pizza in pizzas[0:]:
    print(pizza)

print("My friend's favourite pizzas are:")
for pizza in friend_pizzas[0:]:
    print(pizza)

print("I have a third friend, their favourite pizzas include:")
for pizza in other_pizzas[0:]:
    print(pizza)


# 4.13
buffet = ('Pasta', 'Chicken', 'Beef', 'Olives', 'Oranges')

print("Items included in our buffet: ")
for food in buffet:
    print(food)

buffet = ('Pasta', 'Chicken', 'Macarroni Bites', 'Fish Sticks', 'Oranges')

print("\nOur menu has changed. The new items included in our buffet are: ")
for food in buffet:
    print(food)
