## 2-3. Personal Message:
## Use a variable to represent a person’s name, and print a message to that person. Your message should be simple,
## such as,
## “Hello Eric, would you like to learn some Python today?”

first_name = 'Freya'
middle_names = 'Charlotte Clare'
last_name = 'Juniper-Nine'

print (f"{first_name} {middle_names} {last_name}")
full_name = (f"{first_name} {middle_names} {last_name}")

print (f"Hello, {full_name}, fancy a cup of tea!")

message = f"Hello, {full_name}, fancy a jacket potato!"
print (message)

## 2-4. Name Cases:
## Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase,
## and title case.

print ("\nPrinting the fullname in lower, upper, and title case\n")
print (full_name.lower())
print (full_name.upper())
print (full_name.title())

## 2-5. Famous Quote:
## Find a quote from a famous person you admire.
## Print the quote and the name of its author.
## Your output should look something like the following, including the quotation marks:

## Albert Einstein once said, “A person who never made a mistake never tried anything new.”

famous_person = "Neil Armstrong"
famous_quote = "It's one small leap for man. It's one giant leap for mankind"

print (f"{famous_person} once said, \"{famous_quote}!\"")

## 2-6. Famous Quote 2:
## Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person.
## Then compose your message and represent it with a new variable called message. Print your message.

message = f"{famous_person} once said, {famous_quote}!!!"
print (message)

## 2-7. Stripping Names:
## Use a variable to represent a person’s name, and include some whitespace characters at the beginning
## and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.

new_name = " Arthur Conan Doyle "
another_name = " Prince \n Rogers \t Nelson "

## Print the name once, so the whitespace around the name is displayed.
## Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

print (new_name)
print (new_name.rstrip())
print (new_name.lstrip())
print (new_name.strip())

## Strip doesnt remove tabs or newlines

print (another_name)
rint (another_name.rstrip())
print (another_name.lstrip())
print (another_name.strip())
