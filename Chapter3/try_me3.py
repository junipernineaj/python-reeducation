# 3-8. Seeing the World:
# Think of at least five places in the world you’d like to visit.

# Store the locations in a list.
# Make sure the list is not in alphabetical order.

countries = ['Australia','USA','Japan','Norway','Iceland']

# Print your list in its original order.
# Don’t worry about printing the list neatly, just print it as a raw Python list.

print("Printing my list in its original order")
print(countries)

#Use sorted() to print your list in alphabetical order without modifying the actual list.

print("Printing my list in its alphabetical order - without modifying the list")
print(sorted(countries))

#Show that your list is still in its original order by printing it.

print("And to prove the list is unaltered")
print(countries)

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

print("Printing my list in reverse alphabetical order - without modifying the list")
print(sorted(countries, reverse=True))

#Show that your list is still in its original order by printing it again.

print("And to prove the list is unaltered")
print(countries)

#Use reverse() to change the order of your list. Print the list to show that its order has changed.

print("Reversing my list")
countries.reverse()
print(countries)

#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

print("Putting the list back in its original order by reversing it again")
countries.reverse()
print(countries)

#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

print("Alphabetically sorting countries")
countries.sort()
print(countries)

#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

print("Sorting countries in reverse alphabetical order")
countries.sort(reverse=True)
print(countries)

#3-9. Dinner Guests:
# Working with one of the programs from Exercises 3-4 through 3-7 (page 42),
# use len() to print a message indicating the number of people you are inviting to dinner.

dinner_guests = ['Tom Hardy','Jermaine Clement','Olivia Colman','Tom Cruise']
dinner_guests.insert(0, 'Simon Pegg')
dinner_guests.insert(2, 'Stephen Fry')
dinner_guests.append('Hugh Jackman')
dinner_guests_size = (len(dinner_guests))

print(dinner_guests)
print(f"There are {dinner_guests_size} dinner guests")

#3-10. Every Function: Think of something you could store in a list.
# For example, you could make a list of mountains, rivers, countries, cities, languages,
# or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.