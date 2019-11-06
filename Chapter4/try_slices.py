# Print the message The first three items in the list are:
# Then use a slice to print the first three items from that program’s list.

my_foods = ['pizza', 'falafel', 'carrot cake', 'curry', 'chinese', 'fried chicken']

print("\nThe first three items in my list are: \n")
print (my_foods[:3])

# Print the message Three items from the middle of the list are:
# Use a slice to print three items from the middle of the list.

print("\nThree items from the middle of my list are: \n")
print (my_foods[2:5])

# Print the message The last three items in the list are:
# Use a slice to print the last three items in the list.

print("\nThe last three items from my list are: \n")
print (my_foods[-3:])

# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
my_pizzas = ['pepperoni', 'meat feast', 'vegan hotdog']
friends_pizzas = my_pizzas[:]

print("\nMy Pizzas are:")
print (my_pizzas)
print("\nMy friend's Pizzas are:")
print (friends_pizzas)
# Add a new pizza to the original list.

my_pizzas.append('all day breakfast')
print("\nMy Pizzas are:")
print (my_pizzas)
print("\nMy friend's Pizzas are:")
print (friends_pizzas)

# Add a different pizza to the list friend_pizzas.
# Prove that you have two separate lists.

friends_pizzas.append('ham and pineapple')
print("\nMy Pizzas are:")
print (my_pizzas)
print("\nMy friend's Pizzas are:")
print (friends_pizzas)

# Print the message My favorite pizzas are:, and then use a for loop to print the first list.

print("\nMy favourite Pizzas are:")
for pizza in my_pizzas:
    print(pizza)

# Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list.

print("\nMy friend's favourite Pizzas are:")
for pizza in friends_pizzas:
    print(pizza)

#Make two food lists, and write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favourite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favourite foods are:")
for food in friend_foods:
    print(food)
