# In January 2020 the executive of Google purchased stock options in the company.  
# 	The number of purchased shares were 2,365
# 	The price of the stock was $62.50 per share
# 	He paid stockbroker commission of 2.5% of the amount paid for the stock
# The executive then sold the stock. 
# 	He sold 2,000 shares of the stock
# 	He sold the stock for $78.20 per share
# 	He paid stockbroker commission another 3% of the amount he received for sold stock
# Write a program that displays separate statements for each of the following: 
# 1.	Display the amount of money paid for the stock
# 2.	Display the amount of the commission paid to stockbroker when stock was bought
# 3.	Display the amount the stock was sold for
# 4.	Display the amount of commission paid to stockbroker when stocks were sold
# 5.	Display the amount of money profited or lost from the sold stock (after stockbroker paid) Make sure your print statement clearly states if this is a profit or a loss

# Initializing constant variables
STOCKBROKER_COMMISION_PERCENTAGE_ONE = 0.025
STOCKBROKER_COMMISION_PERCENTAGE_TWO = 0.03

# Initializing variables when the stocks were initially purchased
purchased_shares = 2365
stock_price = 62.50
purchased_stock_amount = 0.0
stockbroker_commision_amount_one = 0.0

# Initializing variables when the stocks were sold
sold_shares = 2000
sold_stock_price = 78.20
sold_stock_amount = 0.0
stockbroker_commision_amount_two = 0.0

grand_total = 0.0

# When buying the stock initially
# Calculating the total amount of the purchase of the shares
purchased_stock_amount = purchased_shares * stock_price

# Calculating the total commision amount when initially buying the stock
stockbroker_commision_amount_one = purchased_stock_amount * STOCKBROKER_COMMISION_PERCENTAGE_ONE

# After Selling the stock
# Calculating the total amount of the sold stock
sold_stock_amount = sold_shares * sold_stock_price

# Calculating the total commision amount when stock was sold
stockbroker_commision_amount_two = sold_stock_amount * STOCKBROKER_COMMISION_PERCENTAGE_TWO

grand_total = (sold_stock_amount + stockbroker_commision_amount_two) - (purchased_stock_amount - stockbroker_commision_amount_one)

# Displaying messages for stock amounts, commission amounts, and total profit
print('The amount paid for the stock is: $', format(purchased_stock_amount, ',.2f'), sep='')
print('The amount of the commission paid to stockbroker when stock was bought is: $', format(stockbroker_commision_amount_one, ',.2f'), sep='')
print('The amount the stock was sold for is: $', format(sold_stock_amount, ',.2f'), sep='')
print('The amount of the commission paid to stockbroker when stock was sold is: $', format(stockbroker_commision_amount_two, ',.2f'), sep='')
print('This was a profit! The amount of money profited is: $', format(grand_total, ',.2f'), sep='')
