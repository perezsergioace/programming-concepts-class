# 7a.

# # creating the constant variable
# EMPLOYEE_RAISE_PERCENTAGE = .025

# # initiating the employees current salaray
# current_salary = 0.0

# # initiating the raise amount for the employee
# employee_raise_amount = 0.0

# # creating the prompt asking to input the employees current salary
# current_salary = float(input('Please enter the employees current salary: '))

# # performing calculations to get the raise amount
# employee_raise_amount = (current_salary * EMPLOYEE_RAISE_PERCENTAGE)

# # displaying the raise amount the employee will get
# print('The raise amount the current employee will get is $', format(employee_raise_amount, ',.2f'), sep='')

# 9

# creating the constant variable
# STANDARD_AMOUNT_OF_COOKIES = 48

# # initiating variables for each ingridient needed for the recipe
# cups_of_sugar = 1.0
# cups_of_butter = 1.5
# cups_of_flour = 2.5

# # initiating the new cups of sugar needed for the new amount of cookies needed
# new_cups_of_sugar = 0.0
# new_cups_of_butter = 0.0
# new_cups_of_flour = 0.0

# cookie_conversion_total = 0.0

# # creating the prompt asking to input the amount of cookies the user wants
# cookies_needed = float(input('Please enter the amount of cookies you want to bake: '))

# cookie_conversion_total = cookies_needed / STANDARD_AMOUNT_OF_COOKIES

# # calculating the new amounts needed for each ingridient
# new_cups_of_sugar = cups_of_sugar * cookie_conversion_total
# new_cups_of_butter = cups_of_butter * cookie_conversion_total
# new_cups_of_flour = cups_of_flour * cookie_conversion_total

# # displaying the number of cups of each ingredient necessary to make that number of cookies. 
# print('You need', format(new_cups_of_sugar, '.2f'), 'cups of sugar' + ' to make', cookies_needed, 'cookies')
# print('You need', format(new_cups_of_butter, '.2f'), 'cups of butter' + ' to make', cookies_needed, 'cookies')
# print('You need', format(new_cups_of_flour, '.2f'), 'cups of flour' + ' to make', cookies_needed, 'cookies')

# 10

# creating the constant variable
AMOUNT_PERCENTAGE_ADDED = 0.05

# initiating variables
amount_of_purchase = 0.0

payment_instalments = 0.0

total_purchase_amount = 0.0

total_of_each_installments = 0.0

# asking the user for the amount of the purchase
amount_of_purchase = float(input('What is the amount of the purchase: '))

# asking the user for the desired number of installments
payment_instalments = float(input('What is the desired number of payment instalments you want to do: '))

# calculating for the total of the purchase and the total for each instalment
total_purchase_amount = (amount_of_purchase * AMOUNT_PERCENTAGE_ADDED) + amount_of_purchase

total_of_each_installments = total_purchase_amount / payment_instalments

# displaying the total for the amount of purchase, the number of instalments and how much each instalment will cost
print('The total amount of the purchase is $', format(total_purchase_amount, ',.2f'), sep='')
print('The total number of instalments entered is', int(payment_instalments))
print('Each instalment will be $', format(total_of_each_installments, ',.2f'), sep='')
