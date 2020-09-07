# creating a variable that will save the input of the excess minutes
excess_minutes = input('Input the amount of excess minutes: ')

# creating a variable that will save the input of the overage fee
overage_fee = input('Input the overage fee: ')

# converting the input of the 'excess_minutes' and the 'overage_fee' into a float class type.
# multiplying the 'excess_minutes' and the 'overage_fee'
monthly_overage_fee = float(excess_minutes) * float(overage_fee)

# Displaying the final amount of the monthly overage fee.
print('Your current monthly overage fee is $', format(monthly_overage_fee, ',.2f'), sep='')

# 9

SALES_TAX = .07

item1 = float(input('Enter price of item 1: '))
item2 = float(input('Enter price of item 2: '))
item3 = float(input('Enter price of item 3: '))
item4 = float(input('Enter price of item 4: '))
item5 = float(input('Enter price of item 5: '))

subtotal = item1 + item2 + item3 + item4 + item5
sales_tax_amount = subtotal * SALES_TAX
final_total = sales_tax_amount + subtotal

print('The subtotal is $', format(subtotal, ',.2f'), sep='')
print('The sales tax amount is $', format(sales_tax_amount, ',.2f'), sep='')
print('The final total is $', format(final_total, ',.2f'), sep='')
