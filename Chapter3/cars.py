#A demonstration in organising lists
#
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#And now sorted - rather than sort

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)


###Reverse ordering a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

###The Length of a list

print("\nFinding the length of a list:\n")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print (len(cars))
