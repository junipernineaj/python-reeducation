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
