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

# item_1 = 12.99
# item_2 = 13.99
# item_3 = 25.99
# item_4 = float(19) # formating this integer into a floating number
# item_5 = 69.99

# new_item_1 = item_1 - (item_1 * SALE_PERCENTAGE) 
# new_item_2 = item_2 - (item_2 * SALE_PERCENTAGE) 
# new_item_3 = item_3 - (item_3 * SALE_PERCENTAGE) 
# new_item_4 = item_4 - (item_4 * SALE_PERCENTAGE) 
# new_item_5 = item_5 - (item_5 * SALE_PERCENTAGE) 

# total_before_tax = new_item_1 + new_item_2 + new_item_3 + new_item_4 + new_item_5
# print(total_before_tax)

# total_cost = (total_before_tax * SALES_TAX) + total_before_tax
# print('Total cost is', format(total_cost, '.2f'))
