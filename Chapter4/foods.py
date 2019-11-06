# Copying a list correctly
#
print("\nCopying a list correctly\n")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Copying a list incorrectly
#
print("\nCopying a list incorrectly\n")

my_foods = ['pizza', 'falafel', 'carrot cake']
new_list = my_foods

my_foods.append('cannoli')
new_list.append('ice cream')

print (my_foods)
print (new_list)
