#A program to manage customer orders and generate bills.

print('''Item\t price(UGX)
Burger\t  25000
Pizza\t  40000
Soda\t  5000
Coffee\t  8000
''')

discount = 0
item_name = input("Select item: ")
quantity = int(input("Enter quantity: "))
price = 0
if item_name =="Burger":
    price = int(25000)
elif item_name == "Pizza":
    price = int(40000)
elif item_name == "Soda":
    price = int(5000)
elif item_name == "Coffee": 
    price = int(8000)
else:
    print("Invalid Request.")

if item_name == "Burger":
    if quantity >= 2:
      discount = 10/100 * 25000
    else:
        discount = 0
else:
    discount = 0
    
print(f"Discount = {discount}")
final_price = price - discount

final_bill = quantity * final_price
print(f"Final Bill: {final_bill} ")
        