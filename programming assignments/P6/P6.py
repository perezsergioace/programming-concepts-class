# 1.) Write an if/else program that determines if a person is old enough to drink.
# (legal age we will assume 21) 

# creating variables
age = 0.0

# creating constant named variables
legal_age = 21

# prompting the user to enter their age
age = int(input('Enter current age: '))

# creatig if else statement to determine if the user's age is at the legal age to drink
# if the age is less than 21 the program will print out a message letting the user know they are not at the legal age to drink
if age < 21:
    print('You are not at the legal age to drink.')
# this else statement will print out a message letting the user know they are at the legal age since the initial if statement did not pass 
else:
    print('You are old enough to drink.')

# 2.) Write an if/else/elif program that asks a user for their favorite color.
# Put a statement in that if the person chooses yellow the program will return “Yellow is also my favorite color” 
# and if the person puts red it will say “Red is the color of my favorite roses.” 
# For all other colors the response should be “That is an interesting color choice.”
# Test the program with yellow, red and two other colors.

# creating variables
favorite_color = 0.0
y_color = 'yellow'
r_color = 'red'

# asking user to input their favorite color
favorite_color = input('Please enter your favorite color: ')

if favorite_color == y_color or favorite_color == r_color:
    if favorite_color == y_color:
        print('Yellow is also my favorite color!')
    else:
        print('Red is the color of my favorite roses!')
else:
    print('That is an interesting color choice.')

# # creating the if/else/elif statement
# # checking whether the string inputed is equal to the stinr 'yellow'
# if favorite_color == y_color:
#     print('Yellow is also my favorite color!')
# # checking whether the string inputed is equal to the string 'red'
# elif favorite_color == r_color:
#     print('Red is the color of my favorite roses!')
# # otherwise any other color inputed will get another message
# else:
#     print('That is an interesting color choice.')

# 3.) Write a program that asks a user for 2 numbers. 
# If the numbers total more than 100 tell them their numbers are greater than 100, 
# if they total less than 100 tell them their numbers total less than 100.  

# creating variables
first_number = 0.0
second_number = 0.0
total = 0.0

# prompting the user to enter two numbers
first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
total = first_number + second_number

# creating the if statment to check whether the sum of the two numbers is greater than 100
# calculating the total of the two numbers
# checking if the total is greater than 100
if total > 100:
    print('The numbers you entered total more than 100!')
else:
    print('The numbers you entered total less than 100!')

# 4.) Draw a flowchart for the each of the decision structures in Questions 1, 2, 3
# *you can include a snapshot or use a program to draw the flowcharts

# 5.) In the book page 155. Wi-Fi Diagnostic Tree. 
# This is an if/else program. NOTHING ELSE. 
# Follow the diagram (page 156) and write the decision structure. 
# You are not declaring variables, you are only writing the Decision Structure of the program.
# You should NOT have any “answers” in your program.
# You should only have : 
# o	If statements
# o	Else statements
# o	Print statements
# o	Response statements 

print('Reboot the computer and try to connect.')
if input('Did that fix the problem? ') == 'yes':
    print('done')
else:
    print('Reboot the router and try to connect.')
    if input('Did that fix the problem? ') == 'yes':
        print('done')
    else:
        print('Make sure the cables between the router & modem are plugged in firmly.')
        if input('Did that fix the problem? ') == 'yes':
            print('done')
        else:
            print('Move the router to a new location and try to connect.')
            if input('Did that fix the problem? ') == 'yes':
                print('done')
            else:
                print('Get a new router.')