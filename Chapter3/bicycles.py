bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# print the first item in a list - expecting trek.

print (bicycles[0])

# You can add string methods - such as title - now you'd expect Trek.

print (bicycles[0].title())

# Offset from 0 - so 1 and 3 will return items 2 and 4 - expecting cannondate and specialized

print(bicycles[1])
print(bicycles[3])

# Last item in a list is in position -1 - expecting specialized

print(bicycles[-1])

# Second last item in a list is in position -2 - expecting redline

print(bicycles[-2])

# Using individual values in from a list

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
