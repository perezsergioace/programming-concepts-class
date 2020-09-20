# 2- Write a program that will ask the user to enter the amount of a purchase. 
#      The program should then compute the state and county sales tax.  
#      Assume the state sales tax is 5 percent and the county sale tax is 2.5 percent.  
# The program should display on separate lines:
# 1.the amount of the purchase, 
# 2. the state sales tax, 
# 3. the county sales tax,
# 4. the total sales tax, 
# 5. The total of the sale (which is the sum of the amount of purchase plus the total sales tax). 
# Make sure all print statements contain full sentences explaining what the figure is and is written so the variable prints the expression.  

# Initializing the variables
purchase_amount = 0.0
state_sales_tax_amount = 0.0
county_sales_tax_amount = 0.0
total_sales_tax_amount = 0.0
grand_total = 0.0

# Initializing the constant named variables
STATE_SALES_TAX = 0.05
COUNTY_SALES_TAX = 0.025

# Asking the customer to input the purchase amount
purchase_amount = float(input('Please enter the amount of the purchase: '))

# Calculating the state sales tax amount by taking the purchase amount and multiplying by the state sales tax percentage
state_sales_tax_amount = purchase_amount * STATE_SALES_TAX

# Calculating the county sales tax amount by taking the purchase amount and multiplying by the county sales tax percentage
county_sales_tax_amount = purchase_amount * COUNTY_SALES_TAX

# Calculating the total sales tax amount by taking the state sales tax amount and adding it to the county sales tax amount
total_sales_tax_amount = state_sales_tax_amount + county_sales_tax_amount

# Calculating the grand total by adding the purchase amount and the total sales tax amount
grand_total = purchase_amount + total_sales_tax_amount

# Displaying the total of the purchase
print('The total of the purchase: $', format(purchase_amount, ',.2f'), sep='')

# Displaying the state sales tax amount
print('The total of the state sales tax: $', format(state_sales_tax_amount, ',.2f'), sep='')

# Displaying the county sales tax amount
print('The total of the county sales tax: $', format(county_sales_tax_amount, ',.2f'), sep='')

# Displaying the total sales tax amount
print('The total sales tax: $', format(total_sales_tax_amount, ',.2f'), sep='')

# Displaying the total of the sale
print('The total of the sale: $', format(grand_total, ',.2f'), sep='')
