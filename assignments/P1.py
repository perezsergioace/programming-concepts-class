# 1

SALES_TAX = .07
SALE_PERCENTAGE = .25

item1 = 12.99 - (12.99 * SALE_PERCENTAGE)
item2 = 13.99 - (13.99 * SALE_PERCENTAGE)
item3 = 25.99 - (25.99 * SALE_PERCENTAGE)
item4 = float(19) - (float(19) * SALE_PERCENTAGE) # formating this integer into a floating number
item5 = 69.99 - (69.99 * SALE_PERCENTAGE)

pre_tax_total = item1 + item2 + item3 + item4 + item5

total_cost = (pre_tax_total * SALES_TAX) + pre_tax_total
print('Total cost is $', format(total_cost, '.2f'), sep='')

# 2

print('\"Isn\'t,\" they said.')
print('\'my dog loves to play\'')
print('\'\"Come over for dinner,\" they said\'')

# 3

print(r'C:\programfiles\user\yourname')
print(r'C:\programfiles\user\sergio')

# 4

print("""\
    Pancakes: How I love them
        -with maple syrup      (needs to be warm)
        -with chocolate chips   (Hershey's is the best)
""")

# 5

print('\'I went to the store to buy pretzels\' \'while I was at the store I also bought chips and salsa\'')

# 6

word = 'programming'
print(word[1])
print(word[5])
print(word[8])

# 7

word = 'programming'
print(word[-1])
print(word[-5])
print(word[-8])

# 8

word = 'programming'
print(word[:2])
print(word[4:])
print(word[-2:-1])
print(word[-2:])

# 9

print(len('formatting'))
print(len('syntax'))
print(len('exponential'))

# 10

COMPANY_NUMBER = 1230987654

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
phone_number = input('Enter phone number including state area code: ')[3:]

print(f"""\
    Hello Applicant!:  
        -You entered: {first_name} as your firt name
        -You entered: {last_name} as your last name
        -This is your phone number without the state area code numbers: {phone_number}

    Thank you {first_name} for applying! If you have any questions please feel free to call us at {COMPANY_NUMBER}.
""")
