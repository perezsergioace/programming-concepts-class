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
favorite_fruit = input('What is your favorite fruti: ')

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

for language in programming_languages:
    print(language)

# creating the for loop

# 5 You are going to write a program that can be used to determine your grade in this class. 
# You will display to the user what percentage they earned in each category, 
# as well as the total combined percentage for the class in a tabbed table format. 
# This should be a reusable program, so do not hard code your grades into it, get input from user. 
