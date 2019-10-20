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
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
```

With no arguments to pop it will take the last value in the list.

You can provide an index position in pop  - ie. pop(0) - or pop(-1)

###Removing an item by value, not position

If you only know the value of the item you want to remove, you can use the remove() method.

```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
```

The remove() method deletes only the first occurrence of the value you specify. If there are more use a loop.

###Organizing a List

The sort() method changes the order of a list permanently.

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
```

will result in:

```python
['audi', 'bmw', 'subaru', 'toyota']
```

You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method.

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
```

###Sorting a List Temporarily with the sorted() function

To maintain the original order of a list but present it in a sorted order, you can use the sorted() function.

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
```

###Printing a List in Reverse Order

To reverse the original order of a list, you can use the reverse() method.

reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list:

Original - and reversed list:

such as:

```python
cars.reverse()
```

```python
['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
```
