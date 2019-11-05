# create an empty list
squares = []

# loop through numbers 1-10
for value in range(1, 11):

# set the variable square as the square of the numbers in the loop

    square = value ** 2
#   print(square)

# append into the list 'squares' the value of the variable 'square'
    squares.append(square)

# then print it out
#    print(squares)

# or print the list  outside the loop
print(squares)

# where ** is the square of


## More concisely

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)


# Simple Statistics with a List of Numbers


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

digits = range(0, 10)
print(min(digits))
print(max(digits))
print(sum(digits))


# List Comprehension
print("\nList comprehension\n")
squares = [value**2 for value in range(1, 11)]
print(squares)