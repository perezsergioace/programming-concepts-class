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

