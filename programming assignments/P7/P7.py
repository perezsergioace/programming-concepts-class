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

if month > 9:
    print('This month is in the fourth quarter.')
elif month <= 9 and month > 6:
    print('This month is in the third quarter.')
elif month <= 6 and month > 3:
    print('This month is in the second quarter.')
else:
    print('This month is in the first quarter.')