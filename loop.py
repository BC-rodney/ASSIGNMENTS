'''in a certain supermarket, a customer can pick up to 5 items. write a program to capture the items taken, quantity and price.
 the program should compute the amount of each item and the total bill of all items'''

totalbill = 0
counter = 1

while True:
    item_taken = input(f"Enter item {counter} or Q to stop: ")
    if item_taken == "Q":
        break

    quantity = int(input("Enter quantity: "))
    price = int(input("Enter price of item: "))
    item_amount = quantity * price
    print(f"Price of item taken = {item_amount}")
    totalbill = totalbill + item_amount
    counter += 1
                                                                
print(f"The total Bill of all items is shs.{totalbill}")

#discount of 10% if total bill is 50000 and above
discount = 0
if totalbill >= 50000 :
    discount = 10/100 * 50000
    print(f"Discount = {discount}")
else: 
    print("No discount")
    
finalbill = totalbill - discount

print(f"Final bill is sh.{finalbill}")



