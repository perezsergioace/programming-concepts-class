# # 1. You are going to figure out which months are in which quarter.
# # Write a program that asks the user for a month as a number between 1-12.
# # The program should display a message indicating whether the month is in the first quarter,
# # the second quarter, the third quarter or the fourth quarter of the year.
# # If the user inputs a number that is not between 1-12 the program should display an error.
# # You will use the if – elif – else  format.  Watch your indenting!!! 

# # creating variables
# month = 0.0

# # initialzing the input for the user to enter a number for the month
# month = int(input('Enter a month as a number between 1-12: '))

# # creating the if - elif - else statement
# if month > 9:
#     print('This month is in the fourth quarter.')
# elif month <= 9 and month > 6:
#     print('This month is in the third quarter.')
# elif month <= 6 and month > 3:
#     print('This month is in the second quarter.')
# else:
#     print('This month is in the first quarter.')

# # 2. Write a program that will ask a user to enter an integer.
# # The program should display “Positive” if the number is greater than 0, 
# # “Negative” if the number is less than 0, 
# # and “Zero” if the number is equal to 0. 
# # The program should then determine if the number is “Even” or “Odd”.  
# # •	You should end up with an if-elif-else, & and if- else statement
# # •	Use % 2 == 0 as the equation to figure out even or odd

# # creating variables
# number = 0.0

# # creating the prompt for the user to enter a number
# number = int(input('Please enter an integer: '))

# # creating the if-elif-else statement to find out if the nubmer is positive or negative or equal to zero
# if number > 0:
#     print('Positive')
# elif number < 0:
#     print('Negative') 
# else:
#     print('Zero')

# # creating the if - else statement to find out if the nubmer is even or odd
# if number % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

# 3. Rectangles:  Area = length x width
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