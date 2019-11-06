# Slicing a list

print("\nThe list\n")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print (players)

print("\nThe first three items in the list\n")
print(players[0:3])

print("\nThe 2nd, 3rd and 4th items in the list\n")
print(players[1:4])

print("\nOmitting the first slice position starts from the beginning of the list\n")
print(players[:4])

print("\nOmitting the last slice position takes you to the end of the list\n")
print(players[3:])

print("\nA negative index returns an element a certain distance from the end of a list;")
print("therefore, you can output any slice from the end of a list.\n"
      "For example, if we want to output the last three players on the roster, we can use the slice players[-3:]:\n")
print(players[-3:])

print("You can include a third value in the brackets indicating a slice. \n"
      "If a third value is included, this tells Python how many items to skip between items in the specified range.")
print(players[0:5:2])

print("\nInstead of looping through the entire list of players Python loops through only the first three names:\n")
for player in players[:3]:
      print(player.title())

print("\nAnd here are the last three players on my team:\n")
for player in players[-3:]:
      print(player.title())
