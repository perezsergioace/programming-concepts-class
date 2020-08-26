# Assignment 1 Notes - The Python Tutorial

## 1. Whetting Your Appetite

Python is simple to use, but it is a real programming language

Python also offers much more error checking than C (another programming language), and, being a very-high-level language, it has high level data types built in, such as flexible arrays and dictionaries.

### Difference Between High and Low Level Languages
> Both High level language and low level language are the programming languages’s types.

> The main difference between *high level language* and *low level language* is that, Programmers can easily understand or interpret or compile the high level language in comparison of machine. On the other hand, Machine can easily understand the low level language in comparison of human beings.

Python allows you to split your program into modules that can be reused in other Python programs

Python comes with a large collection of standard modules

Python is an interpreted language, whcih can save you considerable time during program development because no compilation and linking is necessary.

Python enables programs to be written compactly and readably.

Programs writtne in Python are typically much shorter than equivalent C, C++, or Java programs, for several reasons:
> * the high-level data types allow you to express complex operatins in a single statement;
> * statement grouping is done by indenation instead of beginning and ending brackets;
> * no variable or argument devlarations are necessary

## 2. Using the Python Interpreter

### 2.1 Invoking the Interpreter
The Python interpreter is usually installed as /usr/local/bin/python3.8

### 2.1.2. Interactive Mode
When commands are read from a tty, the interpreter is said to be in *interactive mode*. In this mode it prompts for the next command with the primary prompt, usuall three greater-than signs(>>>); for continuation lines it prompts with the secondary prompt, by defafult three dots (...)

``` python
$ python3.8
Python 3.8 (default, *date*, *time*)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Continuation lines are needed when entering a multi-line construct. As an example, take a look at this if statement:

``` python
>>> the_world_is_flat: True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
```

## 3. An informal Introduction to Python

Comments in Python start with the hash character, **#**, and extend to the end of the physical line.

A comment may appear at the start of a line or following whitespace or code, but nto within a string literal.

Some examples:
``` python
# this is the first comment
spam = 1 # and this is the second comment
         # ... and now a thrid!
test = "# This is not a comment because it's inside quotes."
```

## Using Python as a Calculator
### 3.1.1 Numbers
The interpreter acts as a simple calculator: you can type an expression at it and it will write the value.

Expression syntax is straightforward: the operators +, -, *, and / work just like in most other languages.

``` python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5 # division always returns a floating point number
1.6
```

Integer numbers (e.g. 2, 4, 20) have type **int**(integer)

The ones with fractional part (e.g. 5.0, 1.6) have type **float**.

Division **/** always returns a float.

To do floor division and get an integer result (discarding any fractional result) you can use the **//** operator.

To calculate the remainedr you can use **%**:

``` python
>>> 17 / 3 # classic division returns a float
5.666666666666667
>>> 17 // 3 # floor divion discards the fractional part
5
>>> 17 % 3 # the % operator returns the remainer of the division
2
>>> 5 * 3 + 2 # result * divisor + remainder
17
```

The __**__ operator is used to calculate powers:

``` python
>>> 5 ** 2 # 5 squared
25
>>> 2 ** 7 # 2 to the power of 7
128
```

The equal sign **=** is uded to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt:

``` python
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```

if a variable is not "defined" (assigned a value), trying to use it will give you an error:

``` python
>>> n # try to access an undefined variable
Traceback ( most recent call last):
    File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```

There is full support for floating point; operators with mixed type operands convert the integer operand to floating point:

``` python
>>> 4 * 3.75 - 1
14.0 # becomes a floating number
```

In interactive mode, the last printed expression is assigned to the variable _. This means that when you are using Python as a desk calculator, it is somewhat easier to contine calculations, for example:

``` python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

This variable should be treated as read-only by the user. Don't explicitly assign a value to it.

In addition to int and float, Python supports other types of numbers , such as **Decimal** and **Fraction**

### 3.1.2 Strings
Besider numbers, Python can also manipulate strings, which can be expressed in several ways.

Can be enclosed two ways with the same result:
* 'random sentence surrounded by single quotes'
* "random sentence surrounded by double quotes"

``` python
>>> 'spam eggs' # single quotes
'spam eggs'
>>> 'doesn\'t' # use \' to escape the single quote...
"doesn't"
>>> "doesn't" # ...or use double quotes instead
"doesn't"
```

The **print()** function produces a more readable output, by omitting the enclosign quotes and by printing escaped and special characters:

``` python
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>> s = 'First line.\nSecond line.' # \n means newLine
>>> s # without print(), \n is included in the output
'First line. \nSecond line.'
>>> print(s) # with print(), \n produces a new line
First line.
Second line.
```

If you don't want charactes prefaced by \ to be interpreted as special characters, you can use *raw strings* by adding an **r** before the first quote:

``` python
>>> print('C:\some\name') # here \n means newLine!
C:\some
ame
```
``` python
>>> print(r'C:\some\name') # note the r before the quote
C:\some\name
```

String literals can span multiple lines by using triple-quotes: """...""" or '''...'''.

End of lines are automatically included in the string, but it's possible to prevent this by adding a **\** at the end of the line. The following example:

```python
print("""\
Usage: thingy [OPTIONS]
        -h              Display this usage message
        -H hostname     Hostname to connect to
""")
```
produces the following output(note that the initial newline is not included):

```python
Usage: thingy [OPTIONS]
        -h              Display this usage message
        -H hostname     Hostname to connect to
```

Strings can be concatenated(glued together) with the **+** operator, and repeated with __*__:

```python
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
```

Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically cncatenated.

```python
>>> 'Py' 'thon'
'Python'
```

This feature is partucularly useful when you want to break long strings:

```python
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```

This only works with two literals though, not with variables or expressions:

```python
>>> prefix = 'Py'
>>> prefix 'thon' # can't concatenate a variable and a string literal
    File "<stdin>", line 1
    prefix 'thon'
                ^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
    File "<stdin>", line 1
        ('un' * 3) 'ium'
                       ^
SyntaxError: invalid syntax
```

If you want to concatenate variables or a variable and a literal, use **+**:

```python
>>> prefix + 'thon'
'Python'
```

Strings can be indexed(subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:

```python
>>> word = 'Python'
>>> word[0] # character in position 0
'P'
>>> word[5] # character in position 5
'n'
```
Indices may also be negative numbers, to start counting from the right:

```python
>>> word[-1] # Last character
'n'
>>> word[-2] # second-Last character
'o'
>>> word[-6]
'P'
```

In addition to indexing, *slicing* is also supported. While indexing is used to obtain individual charactes, *slicing* allows you to obtain substring:

```python
>>> word[0:2] # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5] # charactes from position 2 (included to 5 (excluded)
'tho'
```

Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:

```python
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
```

Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.

```python
>>> word[:2] # character from the beginning to position 2 (exluded)
'Py'
>>> word[4:] # characters from position 4 (included) to the end
'on'
>>> word[-2:] # charactes from the seond-Last (included) to the end
'on'
```

Attempting to use an index that is too large will result in an error:

```python
>>> word[42] # the word only has 6 characters
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

However, out of range slice indexes are handled gracefully when used for slicing:

```python
>>> word[4:42]
'on'
>>> word[42:]
''
```

Python strings cannot be changed - they are **immutable**. Therefore, assinging to an indexed position in the string results in an error:

```python
>>> word[0] = 'J'
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'str; object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'str' onject does not support item assignment
```

If you need a different string, you should create a new one:

```python
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
```

The built-in function len() returns the length of a string:

```python
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
```

### 3.1.3 Lists

Python knows a number of compound data types, used to group together other values. The most versatile is the *list*, which can be written as a list of comma-separated values (items) between square brackets. List might contain items of different types, but usually the items all have the same type.

```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```

Like strings (and all other built-in sequence types), lists can be indexed and sliced:

```python
>>> squares[0] # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:] # slicing returns a new list
[9, 16, 25]
```

All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:

```python
>>> squares[:]
[1, 4, 9, 16, 25]
```

Lists also support operations like concatenation:

```python
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81 100]
```

Unlike strings, whch are immutable, lists are a mutable type, i.e. it is possible to change their content:

```python
>>> cubes = [1, 8, 27, 65, 125] # something's wrong here
>>> 4 ** 3 # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64 # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
```

You can also add new item at the end of the ist, by using the **append()** method:

```python
>>> cubes.append(216) # add the cube of 6
>>> cubes.append(7 ** 3) # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```

Assignment to slices is also possible, and this can even cahnge the size of the list or clear it entirely:

```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
```

The built-in function **len()** also applies to lists:

```python
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```

It is possible to nest lists (create lists containing other lists), for example:

```python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```

## 3.2. First Steps Towards Programming
Of course, we can use Python for more complicated tasks than adding two and two together. For instance, we can write an initial sub-sequence of the Fibonacci seris as follows:

```python
>>> # Fibonacci seris:
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8
```

Another Example:

```python
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536
```

Third Example:

```python
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```