# 1   Write and if - else program.  
# ask user if they had fun with Python and return an encouraging message
# creating variables
question = 0.0

# getting user's input
question = input('Did you have fun learning Python(Enter y for yes): ')

# creating the if-else
if question == 'y':
    print('That is great to hear!')
else:
    print('That is too bad, but keep going you will understand it more!')

# 2  Write and if-elif-else program.
# ask the user for their favorite color and return a friendly message
# creating variables
favorite_fruit = 0.0

# getting user's input
favorite_fruit = input('What is your favorite fruit: ')

# creating the if-elif-else
if favorite_fruit == 'peach':
    print('That is my favorite fruit as well!')
elif favorite_fruit == 'apple':
    print('My second favorite fruit')
else:
    print('That is a good fruit.')

# 3  Write a program with a While Loop 
# make the computer count to 5
# creating a variable to control the loop
keep_going = 'y'

while keep_going == 'y':
    for num in range(1, 6):
        print(num)
    
    keep_going = input('Do you want to see me count to 5 again? (Enter y for yes): ')

print('Okay I will stop counting.')

# 4 Write a program with a for loop 
# using a for loop to print out all the programming languages in a list
# creating variables
programming_languages = 0.0

# list
programming_languages = ['Javascript', 'Python', 'Java', 'C', 'C#', 'C++', 'Go', 'Ruby']

print('These are some popular programming languages:')

# creating the for loop
for language in programming_languages:
    print(language)

# 5 You are going to write a program that can be used to determine your grade in this class. 
# You will display to the user what percentage they earned in each category, 
# as well as the total combined percentage for the class in a tabbed table format. 
# This should be a reusable program, so do not hard code your grades into it, get input from user. 

# Reviews/Quizzes/Classwork  30% of grade
# Programming Assignments    40% of grade
# Mid Term                   15% of grade
# Final                      15% of grade

# constant variables
REVIEWS_QUIZZES_CLASSWORK_POSSIBLE_POINTS = 300
PROGRAMMING_ASSIGNMENTS_POSSBILE_POINTS = 400
MID_TERM_POSSIBLE_POINTS = 150
FINAL_POSSIBLE_POINTS = 150

# creating variables
reviews_quizzes_classwork = 0.0
programming_assignments = 0.0
mid_term = 0.0
final = 0.0
reviews_quizzes_classwork_percentage = 0.0
programming_assignments_percentage = 0.0
mid_term_percentage = 0.0
final = 0.0
total_percentage = 0.0


keep_going_grade = 'y'

while keep_going_grade == 'y':
    # getting user's input
    reviews_quizzes_classwork = float(input('Input points from reviews, quizzes, classwork(out of 300): '))
    programming_assignments = float(input('Input points from programming assingments(out of 400): '))
    mid_term = float(input('Input points from mid term(out of 150): '))
    final = int(input('Input point from final(out of 150): '))

    # calculations
    reviews_quizzes_classwork_percentage = ((reviews_quizzes_classwork / REVIEWS_QUIZZES_CLASSWORK_POSSIBLE_POINTS) * .30) 
    programming_assignments_percentage = ((programming_assignments / PROGRAMMING_ASSIGNMENTS_POSSBILE_POINTS) * .40)
    mid_term_percentage = ((mid_term / MID_TERM_POSSIBLE_POINTS) * .15)
    final_percentage = ((final / FINAL_POSSIBLE_POINTS) * .15)
    total_percentage = reviews_quizzes_classwork_percentage + programming_assignments_percentage + mid_term_percentage + final_percentage

    # displaying to the user their grades in a tabbed table
    print('Category\t\t\t\t Percentage')
    print('----------------------------------------------------')
    print('Reviews/Quizzes/Classwork\t\t', format(reviews_quizzes_classwork_percentage, '.0%'))
    print('Programming Assignments\t\t\t', format(programming_assignments_percentage, '.0%'))
    print('Mid Term\t\t\t\t', format(mid_term_percentage, '.0%'))
    print('Final\t\t\t\t\t', format(final_percentage, '.0%'))
    print('Total\t\t\t\t\t', format(total_percentage, '.0%'))

    # creating the conditional statement to determine which grade the user received
    if (total_percentage * 100) >= 90:
        print('Your grade is a A.')
    elif (total_percentage * 100) >= 80:
        print('Your grade is a B.')
    elif (total_percentage * 100) >= 70:
        print('Your grade is a C.')
    elif (total_percentage * 100) >= 60:
        print('Your grade is a D.')
    else:
        print('Your grade is a F.')

    # asking the user to input y if they want to calculate their percentage/letter again
    keep_going_grade = input('Do you want to calculate your grade again(Enter y for yes): ')