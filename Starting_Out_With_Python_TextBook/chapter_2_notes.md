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

