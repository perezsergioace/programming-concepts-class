# Use this formula for the distance that a car travels down the interstate:  
# 	Distance  = Speed * Time 
# The car is traveling 82 miles per hour.  Write a program that displays the following: 
# 1.	The distance the car will travel in 6 hours
# 2.	The distance the car will travel in 10 hours
# 3.	The distance the car will travel in 15 hours.  

# Initiating constant variable for the speed of the car
CAR_SPEED = 82

# Initiating distance variables for each hour
six_hour_distance = 0.0
ten_hour_distance = 0.0
fifteen_hour_distance = 0.0

# Calculating the distance for 6 hours
six_hour_distance = float(CAR_SPEED) * 6

# Calculating the distance for 10 hours
ten_hour_distance = float(CAR_SPEED) * 10

# Calculating the distance for 15 hours
fifteen_hour_distance = float(CAR_SPEED) * 15

# Displaying the distance the car will travel in 6 hours
print('The distance the car will travel in 6 hours is:', format(six_hour_distance, ',.2f'), 'miles')

# Displaying the distance the car will travel in 10 hours
print('The distance the car will travel in 10 hours is:', format(ten_hour_distance, ',.2f'), 'miles')

# Displaying the distance the car will travel in 15 hours
print('The distance the car will travel in 15 hours is:', format(fifteen_hour_distance, ',.2f'), 'miles')
