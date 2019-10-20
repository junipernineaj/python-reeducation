#3-4. Guest List:
# If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.

dinner_guests = ['Tom Hardy','Jermaine Clement','Olivia Colman','Tom Cruise']
message1 = f"Dear {dinner_guests[0]}, would you like to come to dinner?"
message2 = f"Dear {dinner_guests[1]}, would you like to come to dinner?"
message3 = f"Dear {dinner_guests[2]}, would you like to come to dinner?"
message4 = f"Dear {dinner_guests[3]}, would you like to come to dinner?"

print (message1)
print (message2)
print (message3)
print (message4)


#3-5. Changing Guest List:
# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.

#Start with your program from Exercise 3-4.
# Add a print() call at the end of your program stating the name of the guest who can’t make it.

dinner_guests = ['Tom Hardy','Jermaine Clement','Olivia Colman','Tom Cruise']
print (f"\nSadly, {dinner_guests[2]}, can no longer come to dinner.")

#Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#Print a second set of invitation messages, one for each person who is still in your list.

dinner_guests = ['Tom Hardy','Jermaine Clement','Olivia Colman','Tom Cruise']
dinner_guests[2] = 'Noel Fielding'

message1 = f"Dear {dinner_guests[0]}, would you like to come to dinner?"
message2 = f"Dear {dinner_guests[1]}, would you like to come to dinner?"
message3 = f"Dear {dinner_guests[2]}, would you like to come to dinner?"
message4 = f"Dear {dinner_guests[3]}, would you like to come to dinner?"

print (message1)
print (message2)
print (message3)
print (message4)

#3-6. More Guests: You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.

dinner_guests = ['Tom Hardy','Jermaine Clement','Olivia Colman','Tom Cruise']
#Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.

message1 = f"\nDear {dinner_guests[0]}, I have a bigger table, so more people are coming"
message2 = f"Dear {dinner_guests[1]}, I have a bigger table, so more people are coming"
message3 = f"Dear {dinner_guests[2]}, I have a bigger table, so more people are coming"
message4 = f"Dear {dinner_guests[3]}, I have a bigger table, so more people are coming"

print (message1)
print (message2)
print (message3)
print (message4)

#Use insert() to add one new guest to the beginning of your list.

dinner_guests.insert(0, 'Simon Pegg')

#Use insert() to add one new guest to the middle of your list.

dinner_guests.insert(2, 'Stephen Fry')

#Use append() to add one new guest to the end of your list.

dinner_guests.append('Hugh Jackman')

#Print a new set of invitation messages, one for each person in your list.

message1 = f"Dear {dinner_guests[0]}, would you like to come to dinner?"
message2 = f"Dear {dinner_guests[1]}, would you like to come to dinner?"
message3 = f"Dear {dinner_guests[2]}, would you like to come to dinner?"
message4 = f"Dear {dinner_guests[3]}, would you like to come to dinner?"
message5 = f"Dear {dinner_guests[4]}, would you like to come to dinner?"
message6 = f"Dear {dinner_guests[5]}, would you like to come to dinner?"
message7 = f"Dear {dinner_guests[6]}, would you like to come to dinner?"

print (message1)
print (message2)
print (message3)
print (message4)
print (message5)
print (message6)
print (message7)

#3-7. Shrinking Guest List:
# You just found out that your new dinner table won’t arrive in time for the dinner,
# and you have space for only two guests.

#Start with your program from Exercise 3-6.

print (dinner_guests)

uninvited_guest = dinner_guests.pop(0)
message1 = f"Dear {uninvited_guest}, sorry, I'm going to have to change dinner plans"
print (message1)
print (dinner_guests)

uninvited_guest = dinner_guests.pop(0)
message1 = f"Dear {uninvited_guest}, sorry, I'm going to have to change dinner plans"
print (message1)
print (dinner_guests)

uninvited_guest = dinner_guests.pop(0)
message1 = f"Dear {uninvited_guest}, sorry, I'm going to have to change dinner plans"
print (message1)
print (dinner_guests)

uninvited_guest = dinner_guests.pop(0)
message1 = f"Dear {uninvited_guest}, sorry, I'm going to have to change dinner plans"
print (message1)
print (dinner_guests)

uninvited_guest = dinner_guests.pop(0)
message1 = f"Dear {uninvited_guest}, sorry, I'm going to have to change dinner plans"
print (message1)
print (dinner_guests)

# Add a new line that prints a message saying that you can invite only two people for dinner.
#Use pop() to remove guests from your list one at a time until only two names remain in your list.
# Each time you pop a name from your list, print a message to that person letting them know
# you’re sorry you can’t invite them to dinner.

#Print a message to each of the two people still on your list, letting them know they’re still invited.

print (f"Hey, {dinner_guests[0]}, can you still make dinner")
print (f"Hey, {dinner_guests[1]}, can you still make dinner")

#Use del to remove the last two names from your list, so you have an empty list.

dinner_guests.remove('Tom Cruise')
dinner_guests.remove('Hugh Jackman')

#Print your list

print ("Should be an empty list now")
print (dinner_guests)
