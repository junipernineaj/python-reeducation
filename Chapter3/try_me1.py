# 3-1. Names:
# Store the names of a few of your friends in a list called names.
# Print each person’s name by accessing each element in the list, one at a time.

friends = ['Alix','Squeaky','Andrea','Caroline','Vicky']
print (friends[0])
print (friends[1])
print (friends[2])
print (friends[3])
print (friends[4])
print (friends[-1])
print (friends[-2])
print (friends[-3])
print (friends[-4])
print (friends[-5])

# 3-2. Greetings:
# Start with the list you used in Exercise 3-1, but instead of just printing each person’s name,
# print a message to them. The text of each message should be the same, but each message should be
# personalized with the person’s name.

message1 = f"Hey, {friends[0]}, how about another tattoo"
message2 = f"Hey, {friends[1]}, when is your next Among the Echoes gig"
message3 = f"Hey, {friends[2]}, how is your mother"
message4 = f"Hey, {friends[3]}, are you happy your shower is fixed"
message5 = f"Hey, {friends[4]}, had any good ramen lately"

print (message1)
print (message2)
print (message3)
print (message4)
print (message5)

# 3-3. Your Own List:
# Think of your favorite mode of transportation, such as a motorcycle or a car,
# and make a list that stores several examples. Use your list to print a series of statements about these items,
# such as “I would like to own a Honda motorcycle.”

cars = ['BMW','Audi','Mercedes','Range Rover','Jaguar']

print (f"I have just bought a {cars[0]} car")
