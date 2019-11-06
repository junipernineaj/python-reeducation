#Count from 1 to 20 in a for loop
#
for value in range(1, 21):
    print(value)

#One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers

list_of_numbers = []
for value in range(1, 1000001):
    list_of_numbers.append(value)
print(list_of_numbers)

#What is the lowest, highest and sum of the numbers from 1 to a million

print("\nWhat is the lowest, highest and sum of the numbers from 1 to a million\n")
another_list_of_numbers = range(1,1000001)
print(min(another_list_of_numbers))
print(max(another_list_of_numbers))
print(sum(another_list_of_numbers))

#Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20

print("\nOdd numbers in the range 1-20\n")
for value in range(1, 21,2):
    print(value)

#Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

print("\nMultiples of 3 from  1-30\n")
list_multiple_three = []
for value in range(1, 31):
    multiple_of_three=(value*3)
    list_multiple_three.append(multiple_of_three)
    print(multiple_of_three)
print(list_multiple_three)

#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10),
#and use a for loop to print out the value of each cube.

print("\nCubes of numbers from  1-10\n")
cubes = []
for value in range(1, 11):
    cube=(value**3)
    cubes.append(cube)
print(cubes)

#Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

print("\nCube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.\n")

new_cubes = [value**3 for value in range(1, 11)]
print(new_cubes)
