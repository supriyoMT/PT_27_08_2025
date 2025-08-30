# tuple creation        
product = ("Laptop", 50000, 'Black' ,'Samsung', "Electronics")
print('product tuple is :', product)

# fetch 2nd element
print('2nd element is :', product[1])

# Slice and print the last two elements of the product tuple.
print('last two elements of the product tuple is :', product[-2:])

# Check whether "Electronics" is present in the product tuple and print a message.
if "Electronics" in product:
    print("'Electronics' is present in product tuple")

# Create a tuple of 5 product prices: (1000, 1500, 1200, 1100, 900). Count how many times 1000 appears.
product_price = (1000, 1500, 1200, 1100, 900, 1000)    
print(f"1000 appears in product_price for {product_price.count(1000)} no. of times")

# Find and print the maximum and minimum price from the prices tuple.
print(f"Max price is {max(product_price)} and min is {min(product_price)}")

# Use a loop to print each item from the product tuple on a new line.
for prod in product:
    print(f"Product is {prod}")

# Convert the product tuple to a list. Change the price to 55000, then convert it back to a tuple. Print the updated tuple.
product_list = list(product)    
print(product_list)
product_list[1] = 55000
upd_prod_tuple = tuple(product_list)
print(f"Updated prod tuple is {upd_prod_tuple}")

# Add a new item "In Stock" to the product tuple (simulate adding by concatenation).
product = product + ('In Stock',)
print(f"concatenated prod tuple is {product}")

# Remove "Electronics" from the product tuple (by converting to list, removing, and converting back).
product_list = list(product)    
product_list.remove('Electronics')
product = tuple(product_list)
print(f"removed Electronics {product}")

# Unpack the tuple product into three variables and print each variable.
laptop, price, black, sm, instk = product
print(f"laptop {laptop}, price {price}, black {black}, sm {sm}, instk {instk}")

# Create a nested tuple that contains three product tuples inside it. Access and print the name of the 
# second product in the nested tuple.

nest_tuple = ("Laptop1", 50000, 'Black') , ("Laptop2", 60000, 'White') , ("Laptop3", 70000, 'Red')
print("second product in the nested tuple is : ",  nest_tuple[1][1])