# Section 4 Programs: These are to be written as they would need to be written to run in Visual Code or IDLE, not interpreter mode!  

# 1.	Label each part appropriately.  Ask if you have a question! 
# A)	Make a Flowchart
# B)	Write the Program

# Your boss wants you to write a program that will get input from the user and display the information asked using the variable but printing the expression method we have used all semester.  
# You are not creating any fake answers.  
# Boss, “Our restaurant is using ipads now for patrons to pay for their bill.  
# After they have finished their meal the waitress will give them a bill with the total for their entire parties food and drinks.  
# The total will not include the 20% tip or 7% sales tax.  
# Write a program that will ask the user to enter the amount from their bill and then it will calculate the tip and tax.  *tipping is pre-tax   
# Please display to the customer on separate lines: 
# 1.	The total you have entered:
# 2.	The tip on your bill 
# 3.	The tax on your bill 
# 4.	The grand-total of your bill
# 5.	A final line that says “If this is acceptable please sign below” 

# Initializing the variables
bill_amount = 0.0
tip_amount = 0.0
tax_amount = 0.0
grand_total = 0.0

# Initializing the constant named variables
TIP = 0.20
TAX = 0.07

# Asking the customer to input the bill amount
bill_amount = float(input('Please enter the bill amount: '))

# Calculating the tip amount by taking the bill amount and multiplying by the tip percentage(0.20)
tip_amount = bill_amount * TIP

# calculating the tax amount by taking the bill amount and multiplying by the sales tax
tax_amount = bill_amount * TAX

# Calculating the grand total by adding the bill amount, the tip amount and the tax amount
grand_total = bill_amount + tip_amount + tax_amount

# Displaying the message 'The total you have entered:' with the amount entered 
print('The total you have entered: $', format(bill_amount, ',.2f'), sep='')

# Displaying the tip, tax, and the grand total
print('The tip on your bill: $', format(tip_amount, ',.2f'), sep='')
print('The tax on your bill: $', format(tax_amount, ',.2f'), sep='')
print('The grand-total of your bill: $', format(grand_total, ',.2f'), sep='')

#Diplaying the message "If this is acceptable please sign below"
print('"If this is acceptable please sign below"')