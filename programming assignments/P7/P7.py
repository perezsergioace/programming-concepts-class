# 1. You are going to figure out which months are in which quarter.
# Write a program that asks the user for a month as a number between 1-12.
# The program should display a message indicating whether the month is in the first quarter,
# the second quarter, the third quarter or the fourth quarter of the year.
# If the user inputs a number that is not between 1-12 the program should display an error.
# You will use the if – elif – else  format.  Watch your indenting!!! 

# creating variables
month = 0.0

# initialzing the input for the user to enter a number for the month
month = int(input('Enter a month as a number between 1-12: '))

# creating the if - elif - else statement
if month > 9:
    print('This month is in the fourth quarter.')
elif month <= 9 and month > 6:
    print('This month is in the third quarter.')
elif month <= 6 and month > 3:
    print('This month is in the second quarter.')
else:
    print('This month is in the first quarter.')

# 2. Write a program that will ask a user to enter an integer.
# The program should display “Positive” if the number is greater than 0, 
# “Negative” if the number is less than 0, 
# and “Zero” if the number is equal to 0. 
# The program should then determine if the number is “Even” or “Odd”.  
# •	You should end up with an if-elif-else, & and if- else statement
# •	Use % 2 == 0 as the equation to figure out even or odd

# creating variables
number = 0.0

# creating the prompt for the user to enter a number
number = int(input('Please enter an integer: '))

# creating the if-elif-else statement to find out if the nubmer is positive or negative or equal to zero
if number > 0:
    print('Positive')
elif number < 0:
    print('Negative') 
else:
    print('Zero')

# creating the if - else statement to find out if the nubmer is even or odd
if number % 2 == 0:
    print('Even')
else:
    print('Odd')

# 3. Rectangles: Area = length x width
# Write a program that asks for the length and width of 2 rectangles. 
# The program should determine and tell the user which rectangle has the greater area or if they are the same. 
# •	For this go back to chapter 2; declare 6 variables; 
# •	Get your input;
# •	Print statement for the Area of 1 (format precision 2) Ex: print(‘Area of triangle 1 is: ’, format(area1, ‘.2f’))
# •	Print statement for the Area of 2 (format precision 2)
# •	If-elif-else statements with their own print statements

# creating variables
rectangle_one_length = 0.0
rectangle_one_width = 0.0
rectangle_one_area = 0.0

rectangle_two_length = 0.0
rectangle_two_width = 0.0
rectangle_two_area = 0.0

# geting inputs for the length and width of the two rectangles
rectangle_one_length = float(input('Please enter the length of the first rectangle: '))
rectangle_one_width = float(input('Please enter the width of the first rectangle: '))

rectangle_two_length = float(input('Please enter the length of the second rectangle: '))
rectangle_two_width = float(input('Please enter the width of the second rectangle: '))

# calculating the area of each rectangle
rectangle_one_area = rectangle_one_length * rectangle_one_width
rectangle_two_area = rectangle_two_length * rectangle_two_width

print('Area of rectangle 1 is: ', format(rectangle_one_area, '.2f'))
print('Area of rectangle 2 is: ', format(rectangle_two_area, '.2f'))

if rectangle_one_area > rectangle_two_area:
    print('Rectangle one has the greater area.')
elif rectangle_two_area > rectangle_one_area:
    print('Rectangle two has the greater area.')
else:
    print('Rectangle one and Rectangle two have the same area.')

# 4. Assume hot dogs come in packages of 10
# Hot dog buns come in packages of 8
# Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, 
# with the minimal amount of leftovers possible. 
# The program should ask the user for the number of people attending.
# Ask the number of hot dogs each person will be given.

# The program should display the following details: 
# •	The minimum number of packages of hot dogs required
# •	The minimum number of packages of hot dog buns
# •	The number of hot dogs that will be left over
# •	The number of hot dog bun that will be left over 

# This is not a decision structure to start off.  
# Starts as a program as in Chapter 2, that contains decision structures.  
# For this to be correct you should have in this order! : 
# •	7 variables
# •	2 constants
# •	2 get statements
# •	2 calculate statements
# •	#determine if the number of people attending is large enough to require more than one package of hotdogs
# •	If statement for minimum dogs > 0; you will use the modulus for calculation. 
# •	If there is a remainder from above statement another
# •	 if statement that uses != and +=
# •	Else statement 
# •	#determine the number of left over hot dogs, if any
# •	Calculation statement
# •	#determine # of hot dog buns needed
# •	Calculation statement
# •	#determine if the number of people coming are large enough to require more than one package of hot dog buns
# •	If statement  modulus
# •	If statement  != 0   and += 
# •	Else statement 
# •	Calculate the number of buns leftover if any 
# •	Display min packages of hot dogs  (sentence with variable that prints expression) 
# •	Display min packages of buns    (sentence with variable that prints expression)
# •	Display number of hot dogs left over    (sentence with variable that prints expression)
# •	Display number of buns left over        (sentence with variable that prints expression)
