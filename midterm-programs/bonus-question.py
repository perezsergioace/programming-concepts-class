# BONUS 10 Points: (Partial points possible for this bonus) 

# Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula is as follows:   

# 		F =      C + 32
# The program should ask the user to enter a temperature in Celsius, then display the temperature converted to Fahrenheit. 

# To convert temperatures in degrees Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.

# Example: (30°C x 1.8) + 32 = 86°F

# Initializing variables
celsius = 0.0
fahrenheit = 0.0

# Asking useer to enter a temperature in celsius
celsius = float(input('Enter Celsius Temperature to be converted: '))

# Calculating the conversion from celsius to fahrenheit by taking the celcius entered multiplying it by 1.8 and then adding 32
fahrenheit = (celsius * 1.8) + 32

# Displaying the temperature converted to Fahrenheit
print('The temperature converted to Fahrenheit is:', int(fahrenheit), 'degrees')