first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(full_name.upper())
print(full_name.title())
print(full_name.lower())

#You can use f-strings to compose complete messages using the information associated with a variable
print(f"Hello, {full_name.title()}!")

#You can also use f-strings to compose a message, and then assign the entire message to a variable
message = f"Hello, {full_name.title()}!"
print(message)