from datetime import datetime
#meal price calculator 
print()
child_price = float(input("What is the price of a child's meal? $"))
adult_price = float(input("What is the price of an adult's meal? $"))
print()

no_of_children = int(input("How many children are there? "))
no_of_adults = int(input("How many adults are there? "))

print("=" * 50)
#calculating for subtotal
child_total = child_price * no_of_children
adult_total = adult_price * no_of_adults
subtotal = child_total + adult_total

print(f"Subtotal = ${subtotal:.2f}")

print("=" * 50)

#calculating for sales tax
tax_rate = float(input("What is the sales tax rate? "))
tax_amount = subtotal * (tax_rate / 100)
print(f"Sales tax = ${tax_amount:.2f}")

#final meal calculation
total_meal_cost = subtotal + tax_amount 
print(f"Total = ${total_meal_cost:.2f}")

print("=" * 50)

payment = float(input("What is the payment amount? $"))
change = payment - total_meal_cost
print(f"Change = ${change:.2f}")

#formating date and time in string format(strftime method)
print (f"Thank yoou for dining with us! Your meal was calculated on {datetime.now().strftime('%y-%m-%d %H:%M:%S')}")
print("=" * 50)