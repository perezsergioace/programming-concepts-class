# Chapter 7 - List and Tuples

## **7.1 Sequences**
A sequence is an object that holds multiple items of data, stored one after another.

Several types of sequence objects

Tow of the fundamental sequence type:
* Lists
* Tuples

A list is mutable - program can change it's contents
A tuple is immutable - it's contents cannot be changed

## **7.2 Introduction to Lists**
A list is an object that contains multiple data items

They are dynamic data structures, meaning that items may be added to them or removed from them

You can use indexing and slicing

Each item that is stored in a list is called an **element**

Python's built-in **list()** function can convert certain types of objects to lists.

When the operand on the left side of the * symbol is a sequence(such as a list) and the operand on the right side is an integer, it becomes the repetition operator

The repetition operator makes multiple copies of a list and joins them together

You can iterate over a list with a **for loop**

Each element in a list has an index that specifies its position in the list

Function name **len** return the length of a sequence

You can use the **+** operator to concatenate two lists

You can also use the **+=** augmented assignment operator to concatenate one list to another

You can concatenate lists only with other lists

## **7.3 List Slicing**
A slicing expression selects a range of elements from a sequence

A slice is a span of items that are taken from a sequence

## **7.4 Finding Items in Lists with the in Operator**
You can search for an item in a list using the **in** operator

You can use the **in** operator to determine whether an item is contained in a list

*item in list*

You can use the **not in** operator to determine whether an item is not in a list

## **7.5 List Methods and Useful Built-in Functions**
Lists have numerous methods that allow you to work with the elements that they contain

Numerous methods that allow you to add elements, remove elements, change the ordering of elements, and so forth

The **append** method is commonly used to add items to a list

The **index** method returns the index of the first element whose value is equal to item

*index(item)*

if the item is not found in the list, the method raises a **value error** exception

The **insert** method allows you to insert an item into a list at a specific position

The **sort** method rearranges the elements of a list so they appear in ascending order. From lowest to the highest value.

The **remove** method removes an item from the list

The **reverse** method simply reverses the order of the items in the list

Remove an element from a specific index can be accomplished with the **del** statement

The **min** function accepts a sequence, such as a list, as an argument and returns the item that has the lowest value in the sequence

The **max** function returns the item that has the highest value in the sequence

## **7.6 Copying Lists**
To make a copy of a list, you must copy the lists elements

## **7.7 Processing Lists**
To calculate total of list, you use a loop with an accumulator variable. Adding the value of each element to the accumulator.

You can easily pass a list as an argument to a function

A function can return a reference to a list

Saving the contents of a list to a file is a straightforward procedure

Method named **writelines** that writes an entire list to a file

## **7.8 Two-Dimensional Lists**
A two-dimensional list is a list that has other lists as its elements

Lists of lists are also known as **nested lists** or **two dimensional lists**

Two dimensional lists are useful for working with multiple sets of data

## **7.9 Tuples**
A **tuple** is an immutable sequence which means that its contents cannot be changed

Once a tuple is created, it cannot be changed

When you create a tuple, you enclose its elements in a set of parentheses

Like lists, tuples support indexing

Tuples support all the same operations as lists, except those that change the contents of the list

If you want to create a tuple with just one element, you must write a trailing comma after the elements value

If you omit the comma, you will not create a tuple. You will just be creating an integer. In the example below if you don't add the comma:
```python
value = (1) # creates an integer
```

```python
value = (1,) # adding a comma after the single element to create a tuple with just one element.
```

Processing a tuple is faster than processing a list

Tuples are safe

You can store data in one and rest assured that it will not be modified by any code in your program

You can use the built-in **list()** function to convert a tuple to a list

And the built-in **tuple()** function to convert a list to a tuple