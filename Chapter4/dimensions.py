#Tuples
#
print ("\nPrinting position 0 and 1 from the tuple\n")
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Try and reassign a value in a tuple
# dimensions[0] = 250

# Looping through the tuple

print ("\nLooping through the tuple\n")
for dimension in dimensions:
    print(dimension)

# Writing over a Tuple
# Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple.
# So if we wanted to change our dimensions, we could redefine the entire tuple.

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# TryMe Out

# A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

buffetfoods = ('curry', 'chinese', 'pizza', 'sushi', 'fried chicken')

# Use a for loop to print each food the restaurant offers.

for buffetfood in buffetfoods:
    print (buffetfood)

# Try to modify one of the items, and make sure that Python rejects the change.

print("\nThe next line will fail - comment it out - you can't update a tuple\n")
#buffetfoods[0] = 'chips'

# The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

print("\nThe menu is changing so need to update the entire tuple\n")
buffetfoods = ('curry', 'chinese', 'japanese', 'korean', 'fried chicken')
for buffetfood in buffetfoods:
    print (buffetfood)
