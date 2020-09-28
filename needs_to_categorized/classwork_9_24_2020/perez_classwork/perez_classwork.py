# Program 3-5 - loan_qualifier.py

# This program determines whether a bank customer
# qualifies for a loan.

# Constant Variables
MIN_SALARY = 30000.0 # The minimum annual salary
MIN_YEARS = 2 # The minimum years on the job

# Variables
salary = 0.0
years_on_job = 0.0

# Get the customer's annual salary
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job
years_on_job = int(input('Enter the number of ' + 'years employed: '))

# Determine whether the customer qualifies
if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print('You must have been employed', 'for at least', MIN_YEARS, 'years to qualify.')
else:
    print('You must earn at least $', format(MIN_SALARY, ',.2f'), ' per year to qualify.', sep='')

# Program 3-6 grader.py

# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Named constants to represent the grade thresholds
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# variables
score = 0.0

# Gets a test score from the user
score = int(input('Enter your test score: '))

# Determine the grade
if score >= A_SCORE:
    print('Your grade is A.')
else:
    if score >= B_SCORE:
        print('Your grade is B.')
    else:
        if score >= C_SCORE:
            print('Your grade is C.')
        else:
            if score >= D_SCORE:
                print('Your grade is D.')
            else:
                print('Your grade is F.')

# Write a program that asks the user to enter a number of seconds and works as follows:
# * There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal to 60,
    # the program should convert the number of seonds to minutes and seconds.

# * There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3,600,
    # the program should convert the number of seconds to hours, minutes, and seconds.

# * There are 86,400 sedons in a day. If the number of seconds entered by the user is greater than or equal to 86,400,
    # the program should convert the number of seconds to days, hours, minutes, and seconds.

# Constant Variables
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400

# variables
seconds = 0.0

# User enters number of seconds
seconds = int(input('Enter the number of seconds: '))

# Checking if the seconds is greater than the seconds in a day
if seconds >= SECONDS_IN_DAY:
    print('Days:', (seconds // SECONDS_IN_DAY) % 60)
    print('Hours:', (seconds // SECONDS_IN_HOUR) % 24)
    print('Minutes:', (seconds // SECONDS_IN_MINUTE) % 60)
    print('Seconds:', seconds % 60)
# Checking if the seconds is greater than the seconds in a hour
elif seconds >= SECONDS_IN_HOUR:
    print('Hours:', (seconds // SECONDS_IN_HOUR) % 24)
    print('Minutes:', (seconds // SECONDS_IN_MINUTE) % 60)
    print('Seconds:', seconds % 60)
# Checking if the seconds is greater than the seconds in a minute
elif seconds >= SECONDS_IN_MINUTE:
    print('Minutes:', (seconds // SECONDS_IN_MINUTE) % 60)
    print('Seconds:', seconds % 60)
# if none of the conditions are met, printing out the seconds the user input
else:
    print('Seconds:', seconds)
