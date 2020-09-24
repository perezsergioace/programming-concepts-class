# 1
# A. Type this into your program: numbers = [200, 23, 45, 900, 323, 4.5, 209, 12, 28, 1000]
numbers = [200, 23, 45, 900, 323, 4.5, 209, 12, 28, 1000]

# B. Repeat the list 5 times by using the *repetition operator*.
# numbers * 5
numbers = [200, 23, 45, 900, 323, 4.5, 209, 12, 28, 1000] * 5
print(numbers)

# C. Index your list

# [-3]
numbers[-3]
print(numbers[-3])

# [5]
numbers[5]
print(numbers[5])

# [11]
numbers[11]
print(numbers[11])

# D. Use the function that will return the length of your sequence.
len(numbers)
print(len(numbers))

# E. Change elements in your list
# Change 200 to 202
numbers[0] = 202

# Change 28 to 29
numbers[8] = 29

# Print your list
print(numbers)

# 3. You have two lists: numbers2[1, 2, 3, 4, 5] numbers3 = [6, 7, 8, 9, 10, 12]
# Concatenate the lists
numbers2 = [1, 2, 3, 4 , 5]
numbers3 = [6, 7, 8, 9, 10, 11]
numbers4 = numbers2 + numbers3
print(numbers4)

# 3. Slicing using your numbers list
# [:3]
print(numbers4[:3])

# [2:8]
print(numbers4[2:8])

# [:-3]
print(numbers4[:-3])

# [-7:]
print(numbers4[-7:])

# 4. Using the list step = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
step = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# Using slicing with step: print out only the odd numbers
print(step[0::2])

# Using slicing with step: print out only the even numbers
print(step[1::2])
# Using slicing with a step of 3
print(step[1::3])

# Using slicing and step print out every 5th number
print(step[0::5])

# 5 Your list fruit = [apple, banana, melon]
fruit = ['apple', 'banana', 'melon']

# A) append Method: add lemon to the end of the list
fruit.append('lemon')
print(fruit)

# B) insert watermelon after apple
fruit.insert(1, 'watermelon')
print(fruit)

# C) sort the list
fruit.sort()
print(fruit)

# D) reverse the list
fruit.reverse()
print(fruit)

# E) remove lemon from the list
fruit.remove('lemon')
print(fruit)

# 6. del statement: Your list salary = [1000, 500, 45000, 23500, 60245, 1800, 500000]
# * Perfrom all actions
salary = [1000, 500, 45000, 23500, 60245, 1800, 50000]

# a) print list
print(salary)

# b) del index 3
del salary[3]

# c) print list
print(salary)

# d) del index -2
del salary[-2]

# e) print list
print(salary)

# f) del index 8
# del salary[8]
# this will give an error

# g) print list
# print(salary)
# prints out an error

# 7. Copy the original elements salary list in #6 and name the list raises(just a regular copy and paste at this point, not a list copy!)
raises = [1000, 500, 45000, 23500, 60245, 1800, 50000]

# A) perform min sort with the sentence: The lowest raise is
# B) print
print('The lowest raise is', min(raises))

# C) perfrom max sort with the sentence: The maximum raise is
# D) print
print('The maximum raise is', max(raises))

# 8. Using the list in #7 copy it to a new list called raises_2020.
raises_2020 = raises
print(raises)

# 9. Follow all directions and copy and paste the answers as one block.

# A) Create a tuple named school_subjects and fill it with 5 elements.
school_subjects = ('math', 'english', 'science', 'history', 'spanish')

# B) Create a tuple named fav_subjects and fill it with 1 element.
fav_subjects = ('gym',)

# C) print both
print(school_subjects)
print(fav_subjects)

# D) concatenate the lists
my_class_subjects = school_subjects + fav_subjects

# E) print concatenated
print(my_class_subjects)

# 10. Using E from above:

# A) convert tuple to list
my_class_subjects_list = list(my_class_subjects)

# B) print with type
print(type(my_class_subjects_list))

# C) convert the new list back to a tuple
my_class_subjects_back_to_tuple  = tuple(my_class_subjects_list)

# D) print with type
print(type(my_class_subjects_back_to_tuple))