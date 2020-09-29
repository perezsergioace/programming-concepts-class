# **Chapter 3 - Decision Structures and Boolean logic**
## **3.1**
The **if** statement is used to create a decision structure, which allows a program to have more than one path of execution.

The **if** statement causes one or more statements to execute only when a Boolean expression if true.

A **control structure** is a logical decision that controls the order in which a set of statements execute.

A **sequence structure** is a set of statements that execute in the order in which they appear.

**Decision structures** are also know as **selection structures**.

In a decision structure's simplest form, a specific action is performed only if a certain condition exists.

If the condition does not exist, the action is not performed.

In the flowchart, the diamond symbol indicates some condition that must be tested.

The action is **conditionally executed** because it is performed only when a certain condition is true.

Programmers call the type of decision structure show a **single alternative decision structure**.

Because it provides only one alternative path of execution.

In Python, we use the **if** statement to write a single alternative decision structure.

The if clause begins with the word if, followed by a condition, which is an expression that will be evaluated as either true or false.

A colon appears after the **condition**

Block statements - a **block** is simply a set of statement that belong together as a group.

Indentation is required because the Python interpreter uses it tell where the block begins and ends

If the condition is false, the statements in the block are skipped.

The expressions that are tested by the if statements are called **Boolean expressions**.

A **relational operator** determines whether a specific relationship exists between two values.

The **>= and < operators** test for more than one relationship. The >= operator determines whether the operand on its left is greater than or equal to the operand on its right.

The **<= operator** determines whether the operand on its left is less than or equal to the operand on its right.

The **== Operator** determines whether the operand on its left is equal the operand on its right

The **!= Operator** is the not-equal-to operator. It determines whether the operand on its left is not equal to the operand on its right.

## **3.2**
An **if-else** statement will execute one block of statements if its condition is true, or another block if its condition is false.

**Dual alternative decision structure**, which has two possible paths of execution.

One path is taken if a condition is true, and the other path is taken if the condition is false.

When you write an if-else statement, follow these guidelines for indentation:
* Make sure the if clause and the else clause are aligned
* The if clause and else clause are each follow by a block of statements.
* Make sure the statements in the blocks are consistently indented.

## **3.3**
Python allows you to compare strings. This allows you to create decision structures that test the value of a string.

String comparisons are case sensitive

You can also determine whether one string is greater than or less than another string.

## **3.4**
To test more than one condition, a decision structure can be nested inside another decision structure.

The **if-elif-else** statement is never required because its logic can be coded with nested if-else statements.

However, a long series of nested if-else statements has two particular disadvantages when you are debugging code:
* The code can grow and complex and become difficult to understand
* Because of the required indentation, the if-elif-else can become too long.

## **3.5**
The logical **and** operator and the logical **or** operator allow you to connect multiple Boolean expressions to create a compound expression.

The logical **not** operator reverses the truth of a Boolean expression logical operators.

The **and** operator takes two Boolean expressions as operands and creates a compound Boolean expression that is true only when both subexpressions are true.

The **or** operator takes two Boolean expressions as operands and creates a Compound Boolean expression that is true when either of the subexpressions is true.

**Short-Circuit Evaluation**
The **not operator is a unrary operator that takes a Boolean expression as its operand and reverses its logical value.

In other words, if the expression is true, the not operator returns false, and if the expression is false, the not operator returns true.

## **3.6**
A Boolean variable can reference one of two values: **True** or **False**

Boolean variables are commonly used as flags, which indicate whether specific conditions exist.