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