##Working with Lists

Loop through an entire list using just a few lines of code - improving efficiency and removing duplication.

Best practice is to pluralise your list name so you can singularly associate it with a variable.

ie. magicians -> magician.

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
print("And the loop is done.")
```

*NOTE:* The indent required for the print statement - it shows you are 'in the loop'

It is good practice to report you are at the end of the list - perhaps with a print statement.

Because the last line isn't indented it is outside the loop and run after the loop is finished.

###Indentation issues

Always indent the line after the for statement in a loop.

**NOTE** - if you don't Python will remind you with an error.

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)

File "magicians.py", line 3
    print(magician)
        ^
IndentationError: expected an indented block
```

###Making Numerical Lists

####Ranges of numbers

```python
for value in range(1, 5):
    print(value)
```

Note the 'off by one' behaviour - ie. 5 not being printed

That is the loop stops when it reaches the last value you provide.

```python
for value in range(5):
    print(value)
```

providing one value will start the count from 0

####Using range to make a list

```python
numbers = list(range(1, 6))
print(numbers)
```
