## Lists

Storing sets of information in one place.

The list is a collection of items in a specific order.

Square brackets indicate a list - lists[]

When you print a list is is returned including the square brackets.

### Accessing Elements of a List

You can access any element in a list by telling Python the position, or index, of the item desired.

The first item in a list is in position 0

You can also use the string methods on elements of a list.

```python
print (bicycles[0]
print (bicycles[0].title())
```

Last item in a list is [-1]

```python
print (bicycles[-1]
```

Second last item in a list is [-2]

```python
)print (bicycles[-2]
```

### Using individual values from a list

Such as:

```
f"My first bicycle was a {bicycles[0].title()}."
```

### Changing elements of a list

#### Modifying

update position 0 with a different motorcycle

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
```

### Appending

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
```

#### Start with an empty list and build it up

```python
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
```

### Inserting elements into a list

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
```

### Removing elements from a list

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
```

Once it is removed it is gone

###Using the value of a removed item 

The pop() method removes the last item in a list, but it lets you work with that item after removing it.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
```

With no arguments to pop it will take the last value in the list.

You can provide an index position in pop  - ie. pop(0) - or pop(-1)

###Removing an item by value, not position

