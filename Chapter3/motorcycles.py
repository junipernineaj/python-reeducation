# create a list of motorcycles

print ("\nPrinting a list")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# update position 0 with a different motorcycle

print ("\nReferencing one item in a list")
motorcycles[0] = 'ducati'
print(motorcycles)

# Appending to an existing list

print ("\nAppending to a list")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# From an empty list build a list

print ("\nAppending to an empty list")
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)
motorcycles.append('yamaha')
print(motorcycles)
motorcycles.append('suzuki')
print(motorcycles)

# Inserting elements into a list

print ("\nInserting elements into a list")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)

#Removing elements from a list

print ("\nRemoving elements from a list")
motorcycles = ['ducati','honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#Using the value of a removed item with pop()

#With no args pop takes the last value in a list
print ("\nRemoving elements from a list and using it - with pop - no args")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#With a number argument pop takes the positional index value in the list
print ("\nRemoving elements from a list and using it - with pop - positionally")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(-1)
print(f"The last motorcycle I owned was a {last_owned.title()}.")

#Deleting an element by name

print ("\nRemoving an element from a list by name")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

print ("\nUsing the element from the remove method")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")