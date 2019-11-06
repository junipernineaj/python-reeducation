## Working with Lists

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

### Indentation issues

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

### Making Numerical Lists

#### Ranges of numbers

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

#### Using range to make a list

```python
numbers = list(range(1, 6))
print(numbers)
```

#### Simple statistics with sum, min and max

```python
digits = range(0, 10)
print(min(digits))
print(max(digits))
print(sum(digits))
```

#### List Comprehensions

To use this syntax, begin with a descriptive name for the list, such as squares. 

Next, open a set of square brackets and define the expression for the values you want to store in the new list. In this example the expression is value**2, which raises the value to the second power. 

Then, write a for loop to generate the numbers you want to feed into the expression, and close the square brackets. 

The for loop in this example is for value in range(1, 11), which feeds the values 1 through 10 into the expression value**2. 

Notice that no colon is used at the end of the for statement.

```python
squares = [value**2 for value in range(1, 11)]
print(squares)
```

### Working with Parts of a list

#### Slicing a list

To make a slice, you specify the index of the first and last elements you want to work with. 

As with the range() function, Python stops one item before the second index you specify. 

To output the first three elements in a list, you would request indices 0 through 3, which would return elements 0, 1, and 2.

#### Looping through a slice

You can use a slice in a for loop if you want to loop through a subset of the elements in a list.


#### Copying a slice

Define a slice with no parameters and assign it to another list as follows:

```python
new_list = my_foods[:]
```

If we had simply set friend_foods equal to my_foods, we would not produce two separate lists.

ie:

```python
new_list = my_foods
```

You essentially make new_list identical to my_foods so any update to either
will actually update both.

