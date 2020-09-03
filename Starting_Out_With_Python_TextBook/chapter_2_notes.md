# Chapter 2 Input, Processing, and Output

### Topics
* 2.1 Designing a Program
* 2.2 Input, Processing, and Output
* 2.3 Displaying Output with the **print** Function
* 2.4 Comments
* 2.5 Variables
* 2.6 Reading Input from the Keyboard
* 2.7 Performing Calculations
* 2.8 More About Data Output
* 2.9 Named Constants
* 2.10 Introduction to Turtle Graphics

## 2.1 Designing a Program
### Concept:
Programs must be carefully designed they are written. During the design process, programmers use tools such as pseudocode and flowcharts to create models of programs.

### **The Program Development Cycle**
The process of creating a program that works correctly typically requires the five phases. The entire process is know as the *program development cycle*.

Let's take a closer look at each stage in the cycle.

1. **Design the Program**. All the professional programmers will tell you that a program should be carefully designed before the code is actually written. They start by creating a design of the program.
2. **Write the Code**. After designing the program, the programmer begins writing code in a high-level language such as Python.
3. **Correct Syntax Errors**. If the program contains a syntax error, or even a simple mistake such as a misspelled key word, the compiler or interpreter will display an error message indicating what the error is. Once all of the syntax errors and simple typing mistakes have been corrected, the program can be compiled and translated into a machine language program.
4. **Test the Program**. Once the code is in an executable form, it is then tested to determine whether any logic errors exist. A *logic error* is a  mistake that does not prevent the program from running, but cause it to produce incorrect results. (Mathematical mistakes are common cause of logic errors.)
5. **Correct Logic Errors**. If the program produces incorrect results, the programmer *debugs* the code. This means that the programmer finds and corrects logic errors in the program. Sometimes during this process, the programmer discovers that the program's original design must be changed. In this event, the program development cycle starts over and continues until no errors can be found.

### **More About the Design Process**
The process of designing a program is arguably the most important part of the cycle. If your program is designed poorly, eventually you will find yourself doing a lot of work to fix the program.

The process of designing a program can be summarized in the following two steps:

1. Understand the task that the program is to perform.
2. Determine the steps that must be taken to perform the task.

### **Understand the Task That the Program Is to Perform**
It is essential that you understand what a program is supposed to do before you can determine the steps that the program will perform. Typically, a professional programmer gains this understanding by working directly with the customer.

To get a sense of what a program is supposed to do, the programmer usually inter views the customer. During the interview, the customer will describe the task that the program should perform, and the programmer will ask questions to uncover as many details as possible about the task.

The programmer studies the information that was gathered from the customer during the interviews and creates a list of different software requirements. A *software requirement* is simply a single task that the program must perform in order to satisfy the customer. Once the customer agrees that the list of requirements is complete, the programmer can move to the next phase.

### **Determine the Steps That Must Be Taken to Perform the Task**
Once you under stand the task that the program will perform, you begin by breaking down the task into a series of steps that another person can follow.

An algorithm is created, which lists all of the logical steps that must be taken. For example, suppose you have been asked to write a program to calculate and display the gross pay for an hourly paid employee. Here are the steps that you would take:

1. Get the number of hours worked.
2. Get the hourly pay rate.
3. Multiply the number of hours worked by the hourly pay rate.
4. Display the result of the calculation that was performed in step 3.

Of course, this algorithm isn't ready to be executed on the computer. The steps in this list have to be translated into code. Programmers commonly use two tools to help them accomplish this: pseudocode and flowcharts.

### **Pseudocode**
The word "pseudo" means fake, so *pseudocode* is fake code. It is an informal language that has no syntax rules and is not meant to be compiled or executed. Instead, programmers use pseudocode to create models, or "mock-ups," of programs. Because programmers don't have to worry about syntax errors while writing pseudocode, they can focus all of their attention on the program's design. Once a pseudocode can be translated directly to actual code.

Here is an example of how you might write pseudocode for the pay calculating program that was discussed earlier:

*Input the hours worked*
*Input the hourly pay rate*
*Calculate gross pay as hours worked multiplied by pay rate*
*Display the gross pay*

Each statement in the pseudocode represents an operation that can be performed in Python. For example, Python can read input that is typed on the keyboard, perform mathematical calculations, and display messages on the screen.

### **Flowcharts**
Flowcharting is another tool that programmers use to design programs. A *flowchart* is a diagram that graphically depicts the steps that take place in a program.

Notice there are three types of symbols in the flowchart: ovals, parallelograms, and a rectangle. Each of these symbols represents a step in the program, as described here:

* The ovals, which appear at the top and bottom of the flowchart, are called *terminal symbols*. The *Start* terminal symbol marks the program's starting point, and the *End* terminal symbol marks the program's ending point.
* Parallelograms are used as *input symbols* and *output symbols*. They represent steps in which the program reads input or displays output.
* Rectangles are used as *processing symbols*. They represent steps in which the program performs some process on data, such as a mathematical calculation.

The symbols are connected by arrows that represent the "flow" of the program. To step through the symbols in the proper order, you begin at the *Start* terminal and follow the arrows until you reach the *End* terminal.

## **2.2 Input, Processing, and Output**
### **Concept**:
Input is data that the program receives. When a program receives data, it usually processes it by performing some operation with it. The result of the operation is sent out of the program as output.

Computer programs typically perform the following three-step process:

1. Input is received.
2. Some process is performed on the input.
3. Output is produced.

Input is any data that the program receives while it is running. One common form of input is data that is typed on the keyboard. Once input is received, some process, such as a mathematical calculation, is usually performed on it. The results of the process are then sent out of the program as output.

## **2.3 Displaying Output with the *print* Function**
### **Concept**:
You use the *print* function to display output in a Python program.

A *function* is a piece of prewritten code that performs an operation. Python has numerous built-in functions that perform various operations. The most fundamental built-in function is the *print* function, which displays output on the screen.

Here is an example of a statement that executes the *print* function:

```python
print('Hello world')
```

```python
>>> print('Hello world') # pressing enter
Hello world
>>>
```

When programmers execute a function, they say that they are *calling* the function. When you call the *print* function, you type the word *print*, followed by a set of parentheses. Inside the parentheses, you type an *argument*, which is the data that you want displayed on the screen.

Suppose your instructor tells you to write a program that display your name and address on the computer screen.

Example:
```python
>>> print('Kate Austen')
>>> print('123e Full Circle Drive')
>>> print('Asheville, NC 28899')
```

Program Output:
```python
Kate Austen
123 Full Circle Drive
Asheville, NC 28899
```

It is important to understand that the statements in this program execute in the order that they appear, from the top of the program to the bottom. When you run this program, the first statement will execute, followed by the second statement, and followed by the third statement.

### **Strings and String Literals**
Programs almost always work with data of some type.

Example:
```python
'Kate Austen'
'123 Full Circle Drive'
'Asheville, NC 28899'
```

These pieces of data are sequences of characters. In programming terms, a sequence of character that is used as data is called a *string*. When a string appears in the actual code of a program, it is called a *string literal*. In Python code, string literals must be enclosed in quote marks. The quote marks simply mark where the string data begins and ends.

In Python, you can enclose string liters in a set of single-quote marks *(')* or set of double-quote marks *(")*. If you want a string literal to contain either a single-quote or an apostrophe as part of the string, you can enclose the string literal in double-quote marks. Likewise, you can use single-quote marks to enclose a string literal that contains double-quotes as part of the string.

Python also allows you to enclose string literals in triple quotes (either **"""** or **'''**). Triple-quoted strings can contain both single quotes and double quotes as part of the string.

**Example:**
```python
>>> print("""I'm reading "Hamlet" tonight.""")
```

This statement will print
```python
I'm reading "Hamlet" tonight.
```

Triple quotes can also be used to surround multiline strings, something for which single and double quotes cannot be used. Here is an example:
```python
print("""One
Two
Three""")
```

This statement will print:
```python
One
Two
Three
```

## **2.4 Comments**
### **Concept:**
Comments are notes of explanation that document lines or sections of a program. Comments are part of the program, but the Python interpreter ignores them. They are intended for people who may be reading the source code.

Comments are short notes placed in different parts of a program, explaining how those parts of the program work. They are also ignored by the Python interpreter. Comments are intended for any person reading a program's code, not the computer.

In Python, you begin a comment with the *#* character. When the Python interpreter sees a *#* character, it ignores everything from that character to the end of the line.

Example:
**Input**
```python
# this program displays a person's 
# name and adress.
>>> print('Kate Austen')
>>> print('123 Full Circle Drive')
>>> print('Asheville, NC 28899')
```

**Output**
```python
Kate Austen
123 Full Circle Drive
Asheville, NC 28899
```

Programmers commonly write end-line comments in their code. An *end-line comment* is a comment that appears at the end of a line of code. It usually explains the statement that appears in that line.

Example:
**Input**
```python
>>> print('Kate Austen') # Display the name.
>>> print('123e Full Circle Drive') # Display the address.
>>> print('Asheville, NC 28899') # Display the city, state, and ZIP
```

**Output**
```python
Kate Austen
123 Full Circle Drive
Asheville, NC 28899
```

It is crucial that you take the extra time to write comments. They can save you and others time in the future when you have to modify or debug the program. Large and complex programs can be almost impossible to read and understand if they are not properly commented.

## **2.5 Variables**
### **Concept**:
A variable is a name that represents a value stored in the computer's memory.

Programs usually store data in the computer's memory and perform operations on that data.

Programs use variables to access and manipulate data that is stored in memory. A *variable* is a name that represents a value in the computer's memory.

For example, a program that calculates the sales tax on a purchase might use the variable name **tax** to represent that value in memory. And a program that calculates the distance between two cities might use the variable name **distance** to represent that value in memory. When a variable represents a value in the computer's memory, we say that the variable *references the value.

### **Creating Variables with Assignment Statements**
You use an *assignment statement* to create a variable and make it reference a piece of data. Here is an example of an assignment statement:

```python
>>> age = 25
```

After this statement executes, a variable named **age** will be created, and it will reference the value 25. In the example below, think of the value 25 as being stored somewhere in the computer's memory. The arrow that points from **age** to the value **25** indicates that the name **age** references the value.

> age ----> 25

Assignment statements are written in the following general format:

> variable = expression

The equal sign (=) is known as the *assignment operator*. In the general format, **variable** is the name of a variable and **expression** is a value, or any piece of code that results in a value. After an assignment statement executes, the variable listed on the left side of the **=** operator will reference the value given on the right side of the **=** operator.

Typing assignment statements in interactive mode:
```python
>>> name = Tom # Enter
>>> age = 23
```

Next, you can use the **print** function to display the values referenced by the variables created above.
```python
>>> print(name)
Tom
>>> print(age)
23
```

When you pass a variable as an argument to the **print** function, you do not enclose the variable name in quote marks. To demonstrate why, look at the following interactive session:
```python
>>> print('name')
name
>>> print(name)
Tom
```

In an assignment statement, the variable that is receiving the assignment must appear on the left side of the **=** operator. As show in the following interactive session, an error occurs if the item on the left side of the **=** operator is not a variable:
```python
>>> 25 = age # Enter
SyntaxError: can't assign to literal
>>>
```

In the next sample program, create two variable: top_speed and distance:
```python
# Create two variables: top_speed and distance.
top_speed = 160
distance = 300

# Display the values referenced by the variables.
print('The top speed is')
print(top_speed)
print('The distance traveled is')
print(distance)
```
**Output**
```python
The top speed is
160
The distance traveled is
300
```

#### **Warning!**
You cannot use a variable until you have assigned a value to it. An error will occur if you try to perform an operation on a variable, such as printing it, before it has been assigned a value.

### **Variable Naming Rules**
Although you are allowed to make up your own names for variable you must follow these rules:

* You cannot use one of Python's key words as a variable name.
* A variable name cannot contain spaces.
* The first character must be one of the letters **a** through **z** or **A** through **Z**, the digits 0 through 9, or underscores.
* Uppercase and lowercase characters are distinct. This means the variable name **ItemsOrdered** is not the same as **itemsordered**.

In addition to following these rules, you should always choose names for your variables that give an indication of what they are used for.

Because a variable's name should reflect the variable's purpose, programmers often find themselves creating the names that are made of multiple words. For example, consider the following variable names:

```python
grosspay
payrate
hotdogssoldtoday
```

Unfortunately, these names are not easily read by the human eye because the words aren't separated. Because we can't have spaces in variable names, we need to find another way to separate the words in a multiword variable name and make it more readable to the human eye.

One way to do this is to use the under score character to represent a space. For example, the following variable names are easier to read than those previously show:

```python
gross_pay
pay_rate
hot_dogs_sold_today
```

This style of naming variables is popular among Python programmers, and is the style we will use in this book. The are other popular styles, however, such as the *camelCase* naming convention. camelCase names are written in the following manner:

* The variable name begins with lowercase letters.
* The first character of the second and subsequent words is written in uppercase

For example, the following variable names are written in camelCase:

```javascript
grossPay
payRate
hotDogsSoldToday
```

#### **Note:**
This style of naming is called camelCase because the uppercase characters that appear in a name may suggest a camel's humps.

### **Displaying Multiple Items with the *print* Function**
Python allows us to display multiple items with one call the **print** function. A programmer simply has to separate the items with commas as shown in the example below.

```python
# This program demonstrates a variable.
>>> room = 503
>>> print('I am staying in room number', room)
```

In line 3, we passed two arguments to the **print** function. The first argument is the string literal 'I am staying in room number', and the second argument is the **room** variable.

**Program Output**
```python
I am staying in room number 503
```

When the **print** function executed, it displayed the values of the two arguments in the order that we passed them to the function. Notice the **print** function automatically printed a space separating the two items. When multiple arguments are passed to the **print** function, they are automatically separated by a space when they are displayed on the screen.

### **Variable Reassignment**
Variables are called "variable" because they can reference different values while a program is running. When you assign a value to a variable, the variable will reference that value until you assign it a different value.

For example, look at the example below. The statement in line 3 creates a variable named **dollars** and assigns it the value 2.75. Then, the statement in line 8 assigns a different value, 99.95, to the **dollars** variable.

> The dollars variable after line 3 executes.
> 
> dollars ----> 2.75
>
> The dollars variable after line 8 executes
>
> the old value is still here 2.75
> 
> dollars ----> 99.95

The old value, 2.75, is still in the computer's memory, but it can no longer be used because it isn't referenced by a variable. When a value in memory is no longer referenced by a variable, the Python interpreter automatically removes it from memory through a process known as **garbage collection**.

**variable_demo4.py**
```python
# this program demonstrates variable reassignment.
# Assign a value to the dollars variable.
dollars = 2.75
print('I have', dollars, 'in my account.')

# Reassign dollars so it references
# a different value.
dollars = 99.95
print('But now I have', dollars, 'in my account!')
```

**Program Output**
```python
I have 2.75 in my account.
But now I have 99.95 in my account!
```

### **Numeric Data Types and Literals**
Because different types of numbers are stored and manipulated in different ways, Python uses *data types* to categorize values in memory. When an integer is stored in memory, it is classified as an **int**, and when a real number is stored in memory, it is classified as a **float**.

A number that is written into a program's code is called a *numeric literal*. When the Python interpreter reads a numeric literal in a program's code, it determines its data type according to the following rules:

* A numeric literal that is written as a whole number with no decimal point is considered an **int**. Examples are **7**, **124**, and **-9**.
* A numeric literal that is written with a decimal point is considered a **float**. Examples are **1.5**, **3.14159**, and **5.0**.

So, the following statement cause the number 503 to be stored in memory as an **int**:

```python
room = 503
```

And the following statement causes the number 2.75 to be stored in memory as a **float**.

When you store an item in memory, it is important for you to be aware of the item's data type. As you will see, some operations behave differently depending on the type of data involved, and some operations can only be performed on values of a specific data type.

You can use the built-in **type** function in interactive mode to determine the data type of a value. For example, look at the following session:

```python
>>> type(1) # Enter
<class 'int'>
>>>
```
In this example, the value 1 is passed as an argument to the **type** function. The message that is displayed on the next line, indicates that the value is an **int**. Here is another example:

```python
>>> type(1.0) # Enter
<class 'float'>
>>>
```

In this example, the value 1.0 is passed as an argument to the **type** function. The message that is displayed on the next line, **<class 'float'>, indicates that the value is a float.

You cannot write currency symbols, spaces, or commas in numeric literals. For example, the following statement will cause an error:
```python
value = $4,567.99 # Error!
```

This statement must be written as:
```python
value = 4567.99 # Correct
```

### **Storing Strings with the *str* Data Type**
Python also has a data type named **str**, which is used for storing strings in memory.

**Example**:
```python
# Create variables to reference two strings.
first_name = 'Kathryn'
last_name = 'Marino'

# Display the values referenced by the variables.
print(first_name, last_name)
```

**Program Output**
```python
Kathryn Marino
```

### **Reassigning a Variable to Different Type**
The Python interpreter keeps track of the variable names that you create and the pieces of data to which those variable names refer. Any time you need to retrieve one of those pieces of data, you simply use the variable name that refers to it.

A variable in Python can refer to items of any type. After a variable has been assigned an item of one type, it can be reassigned an item of a different type.

## **2.6 Reading Input from the Keyboard**
### **Concept:**
Programs commonly need to read input typed by the user on the keyboard. We will use the Python functions to do this.

When a program reads data from the keyboard, usually it stores that data in a variable so it can be used later by the program.

Python's built-in **input** function is used to read input from the keyboard. The **input** function reads a piece of data that has been entered at the keyboard and returns that piece of data, as a string, back to the program. You normally use the **input** function in an assignment statement that follows this general format:

```python
variable = input(prompt)
```

In the general format, **prompt** is a string that is displayed on the screen. The string's purpose is to instruct the user to enter a value. Here is an example of a statement that uses the **input** function to read data from the keyboard:

```python
name = input('What is your name?')
```

When this statement executes, the following things happen:

* The string **'What is your name? '** is displayed on the screen.
* The program pauses and waits for the user to type something on the keyboard and then to press the Enter key.
* When the Enter key is pressed, the data that was typed is returned as a string and assigned to the **name** variable.

**Example**:
```python
>>> name = input('What is your name? ')
What is your name? # Holly # Enter
>>> print(name) # Enter
Holly
```

**string_input.py**
```python
# Get the user's first name.
first_name = input('Enter your first name: ')

# Get the user's last name.
last_name = input('Enter your last name: ')

# Print a greeting to the user.
print('Hello', first_name, last_name)
```

**Program Output(with input shown in bold)
```python
Enter your first name: Vinny # Enter
Enter your last name: Brown # Enter
Hello Vinny Brown
```

Take a closer look in line 2 at the string we used as a prompt:
```python
'Enter your first name: '
```

Notice the last character in the string, inside the quote marks, is a space. The same is true for the following string, used as prompt in line 5:
```python
'Enter your last name: '
```

We put a space character at the end of each string because the **input** function does not automatically display a space after the prompt. When the user begins typing characters, they appear on the screen immediately after the prompt. Making the last character in the prompt a space visually separates the prompt from the user's input on the screen.

### **Reading Numbers with the *input* function**
The **input** function always returns the user's input as a string, even if the user enters numeric data. For example, you suppose you call the **input** function, type the number 72, and press the Enter key. The value that is returned from the **input** function is the string '72'. This can be a problem if you want to use the value in a math operation. Math operations can be performed only on numeric values,not strings.

Fortunately, Python has built-in functions that you can use to convert a string to a numeric type.

For example, suppose you are writing a payroll program and you want to get the number of hours that the user has worked. Look at the following code:

```python
string_value = input('How many hours did you work? ')
hours = int(string_value)
```

The first statement gets the number of hours from the user and assigns that value as a string to the **string_value** variable. The second statement calls the **int()** function, passing string_value as an argument. The value referenced by **string_value** is converted to an **int** and assigned to the **hours** variable.

This example illustrates how the **int()** functions works, but it is inefficient because it creates two variables: one to hold the string that is returned from the **input** function, and another to hold the integer that is returned from the **int()** function. The following code shows a better approach. This one statement does all the work that the previously show two statements do, and it creates only one variable:

```python
hours = int(input('How many hours did you work? '))
```

This one statement uses nested function calls. The value that is returned from the **input** function is passed as an argument to the **int()** function. This is how it works:

* It calls the **input** function to get a value entered at the keyboard.
* The value that is returned from the **input** function (a string) is passed as an argument to the **int()** function.
* The **int** value that is returned from the **int()** function is assigned to the **hours** variable.

After this statement executes, the **hours** variable is assigned the value entered at the keyboard, converted to an **int**

**inpur.py Example**:
```python
# Get the user's name, age, and income.
name = input('What is your name? ')
age = int(input('What is your age? '))
income = float(input('What is your income? '))

# Display the data.
print('Here is the data you entered:')
print('Name:', name)
print('Age:', age)
print('Income:', income)
```

**Program Output**
```python
What is your name? Chris
What is your age? 25
What is your income? 75000.0
Here is the data you entered:
Name: Chris
Age: 25
Income: 75000.0
```

**Breakdown of Example Code**
* Line 2 prompts the user to enter his or her name. The value that is entered is assigned, as a string, to the **name** variable.
* Line 3 prompts the user to enter his or her age. The value that is entered is converted to an **int** and assigned to the **age** variable.
* Line 4 prompts the user to enter his or her income. The value that is entered is converted to a **float** and assigned to the **income** variable.
* Lines 7 through 10 display the values that the user entere.

The **int()** and **float()** functions work only if the item that is being converted contains a valid numeric value. If the argument cannot be converted to the specified data type, an error know as an exception occurs. An *exception* is an unexpected error that occurs while a program is running, causing the program to halt if the error is not properly dealt with. For example, look at the following interactive mode session:

```python
>>> age = int(input('What is your age? '))
What is your age? xyz
Traceback (most recent call last):
 File "<pyshell#81>", line 1, in <module>
 age = int(input('What is your age? '))
ValueError: invalid literal for int() with base 10: 'xyz'
>>>
```

**Note**:
In this section, we mentioned the user. The *user* is simply any hypothetical person that is using a program and providing input for it. The user is sometimes called the *end user*.

## **2.7 Performing Calculations**
### **Concept:**
Python has numerous operators that can be used to perform mathematical calculations.

A programmer's tools for performing calculations are *math operators*.

A *math expression* performs a calculation and gives a value.

The following is an example of a simple math expression:
```python
12 + 2
```

The values on the right and left of the + operator are called *operands. These are values that the + operator adds together.

Variables may also be used in a math expression. For example, suppose we have two variables name *hours* and *pay_rate*. The following math expression uses the * operator to multiply the value referenced by the *hours* variable by the value referenced by the *pay_rate* variable:
```python
hours * pay_rate
```

When we use a math expression to calculate a value, normally we want to save that value in memory so we can use it again in the program.

### **Spotlight: Calculating a Percentage**
If you are writing a program that works with a percentage, you have to make sure that the percentage's decimal point is in the correct location before doing any math with the percentage.

Before you perform any calculations with such a percentage, you have to divide it by 100 to move its decimal point two places to the left.

Calculate the sale price of an item after the discount is subtracted. Here is the algorithm:

1. Get the original price of the item.
```python
original_price = float(input("Enter the item's original price: "))
```

2. Calculate 20 percent of the original price. This is the amount of the discount.
```python
discount = original_price * 0.2
```

3. Subtract the discount from the original price. This is the sale price.
```python
sale_price = original_price - discount
```

4. Display the sale price.
```python
print('The sale price is', sale_price)
```

**Program Output**
```python
Enter the item's original price: 100.00 # Enter
The sale price is 80.0
```

### **Floating-Point and Integer Division**
Python has two different division operators. The **/** operator performs floating-point division, and the **//** operator performs integer division.

The difference between them is that the **/** operator gives the result as a floating-point value, and the **//** operator gives the result as a whole number.

**The / operator**
```python
>>> 5 / 2 # Enter
2.5
>>>
```

**The // operator**
```python
>>> 5 // 2 # Enter
2
>>>
```

* When the result is positive, it is *truncated*, which means that its fractional part is thrown away.
* When the result is negative, it is rounded *away from zero* to the nearest integer.
```python
>>> -5 // 2 # Enter
-3
>>>
```

### **Operator Precedence**
You can write statements that use complex mathematical expressions involving several operators. Python follows the same order of operations that you learned in math class.

First, operations that are enclosed in parentheses are performed first. Then, when two operators share an operand, the operator with the higher *precedence* is applied first. The precedence of the math operators, from highest to lowest, are:

1. Exponentiation: **
2. Multiplication, division, and remainder: * / // %
3. Addition and subtraction: + -


[Article on Order of Operations](https://www.mathsisfun.com/operation-order-pemdas.html)

### **Grouping with Parentheses**
Parts of a mathematical expression may be grouped with parentheses to force some operations to be performed before others

### **The Exponent Operator**
Python also provides an exponent operator. Two asterisks written together(**) is the exponent operator, and its purpose is to raise a number to a power. 

### **The Remainder Operator**
In Python, the % symbol is the remainder operator. (This is also known as the *modulus operator*) The remainder operator performs division, but instead of returning the quotient, it returns the remainder.

### **Converting Math Formulas to Programming Statements**
When converting some algebraic expressions to programming expressions, you may have to insert parentheses that do not appear in the algebraic expression.

### **Mixed-Type Expressions and Data Type Conversion**
When you perform a math operation on two operands, the data type of the result will depend on the data type of the operands. Python follows these rules when evaluating mathematical expressions:

* When an operation is performed on two **int** values, the result will be an **int**
* When an operation is performed on two **float** values, the result will be a **float**
* When an operation is performed on an **int** and a **float**, the **int** value will be temporarily converted to a **float** and the result of the operation will be a **float**.(An expression that uses operands of different data types is called a *mixed-type expression*.)

The **int** to **float** conversion that takes place in the previous statement happens implicitly. If you need to explicitly perform a conversion, you can use either the **int()** or **float()** functions.

### **Breaking Long Statements into Multiple Lines**
Most programming statements are written on one line. If a programming statement is too long, however, you will not be able to view all of it in your editor window without scrolling horizontally. In addition, if you print your program code on paper and one of the statements is too long to fit on one line, it will wrap around to the next line and make the code difficult to read.

Python allows you to break a statement into multiple lines by using the *line continuation character*, which is a backslash(\). You simple type the backslash character at the point you want to break the statement, then press the Enter key.

For example, here is a statement that performs a mathematical calculation and has been broken up to fit on two lines:
```python
result = var1 * 2 + var2 * 3 + \
         var3 * 4 + var4 * 5
```

Python also allows you to break any part of a statement that is enclosed in parentheses into multiple lines without using the line continuation character.

The following code shows an example of this:
```python
total = (value1 + value2 +
        value3 + value4 +
        value5 + value6)
```

## **2.8 More About Data Output**
In this section, you will learn more details about the Python **print** function, and you'll see techniques for formatting output in specific ways.

### **Suppressing the *print* Function's Ending Newline**
The **print** function normally display a line of output.

If you do not want the **print** function to start a new line of output when it finishes displaying its output, you can pass the special argument **end=' '** to the function, as show in the following code:
```python
print('One', end= ' ')
print('Two', end= ' ')
print('Three')
```

Here is the output of these statements:
```python
One Two Three
```

Sometimes, you might not want the **print** function to print anything at the end of its output, not even a space. If that is the case, you can pass the argument **end=''** to the **print** function.

### **Specifying an Item Separator**
When multiple arguments are passed to the **print** function, they are automatically separated by a space when they are displayed on the screen.

Here is an example, demonstrated in interactive mode:
```python
>>> print('One', 'Two', 'Three')
One Two Three
>>>
```

If you do not want a space printed between the items, you can pass the argument **spe=''** to the **print** function, as show here:
```python
>>> print('One', 'Two', 'Three', sep='')
OneTwoThree
>>>
```

You can also use this special argument to specify a character other than the space to separate multiple items. Here is an example:
```python
>>> print('One', 'Two', 'Three', sep='*')
One*Two*Three
>>>
```

Notice in this example, we passed the argument sep='*' to the **print** function. This specifies that the printed items should be separated with the * character.

### **Escape Characters**
An *escape character* is a special character that is preceded with a backslash(\), appearing inside a string literal.

For example, **\n** is the newline escape character. When the **\n** escape character is printed, it isn't displayed on the screen. Instead it causes output to advance to the next line. For example, look at the following statement:
```python
print('One\nTwo\nThree')
```

When this statement executes, it displays
```python
One
Two
Three
```

Python recognizes several escape characters.

### **Displaying Multiple Items with the + Operator**
Earlier in this chapter, you saw that the + operator is used to add two numbers. When the + operator is used with two strings, however, it performs **string concatenation**. This means that is appends one string to another. For example, look at the following statement:
```python
print('This is ' + 'one string.')
```

This statement will print
```python
This is one string.
```

String concatenation can be useful for breaking up a string literal so a lengthy call to the **print** function can span multiple lines.

### **Formatting Numbers**
You might not always be happy with the way that numbers especially floating-point numbers, are displayed on the screen. When a floating-point number is displayed by the **print** function, it can appear with up to 12 significant digits.

When you can call the built-in **format** function, you pass two arguments to the function: a numeric value and a format specifier. The *format specifier* is a string that contains special characters specifying how the numeric value should be formatted. Let's look at an example:
```python
format(12345.6789, '.2f')
```

The first argument, which is the floating-point number 12345.6789, is the number that we want to format. The second argument, which is the string '.2f' , is the format specifier. Here is the meaning of its contents:

* The .2 specifies the precision. It indicates that we want to round the number to two decimal places.
* The f specifies that the data type of the number we are formatting is a floating-point number.

The **format** function returns a string containing the formatted number.
```python
>>> print(format(12345.6789, '.2f'))
12345.68
>>>
```

Notice the number is rounded to two decimal places. The following
example shows the same number, rounded to one decimal place:

```python
>>> print(format(12345.6789, '.1f'))
12345.7
>>>
```

### **Formatting in Scientific Notation**
If you prefer to display floating-point numbers in scientific notation, you can use letter **e** or the letter **E** instead of **f**. Here are some example:
```python
>>> print(format(12345.6789, 'e'))
1.234568e+04
>>> print(format(12345.6789, '.2e'))
1.23e+04
>>>
```

### **Inserting Comma Separators**
If you want the number to be formatted with comma separators, you can insert a comma into the format specifier, as shown here:
```python
>>> print(format(12345.6789, ',.2f'))
12,345.68
>>>
```

Here is an example that formats an even larger number:
```python
>>> print(format(123456789.456, ',.2f'))
123,456,789.46
>>>
```
