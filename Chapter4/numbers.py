# Number 1 to 4 by providing two numbers
for value in range(1, 5):
    print(value)

# Number from 0 to 4 by providing only one number
for value in range(5):
    print(value)

# Creating a list from a range of numbers
# No for loop - no indent

numbers = list(range(1, 6))
print(numbers)

#A range with an interval provided as the third parameter

even_numbers = list(range(2, 11, 3))
print(even_numbers)