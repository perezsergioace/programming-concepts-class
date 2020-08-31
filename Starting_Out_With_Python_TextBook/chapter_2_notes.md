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

### **Understand the Task That the Program Is to Perform
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