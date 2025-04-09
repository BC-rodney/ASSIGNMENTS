#A program to determine the selling price and profit margin of items.
cost_price = int(input("Cost Price = "))

transport_cost = int(input("Transport Cost = "))

selling_price = cost_price + (5/100 * cost_price) + (2/100 * transport_cost)

print(f"Selling Price ={selling_price}")

profit = selling_price - cost_price

print(f"Profit = {profit}")
      
if profit > 0 :
    print("Profit Available")
else :
    print("Loss")
