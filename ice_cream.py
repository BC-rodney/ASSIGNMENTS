#A program  to customise ice cream orders and calculate cost of ice cream automatically
print('''\tWhat would you like your ice cream to be served in :
       Container\tUGX
      1. Cone\t\t500
      2. Cup\t\t800
      ''')
item_code = int(input("What would you like your ice cream to be served in (1 or 2) :"))
containername = ""
if item_code == 1:
    containername == "Cone"
    containerprice = 500
elif item_code == 2 :
    containername == "Cup"
    containerprice = 800
else:
    print("Invalid Request")
print(f"Container Price = {containerprice}")


scoop_price = 0
numberofscoops = int(input("How many scoops would you like.(between 1 and 4): "))
if numberofscoops == 1:
    scoop_price = 1000
elif numberofscoops == 2:
    scoop_price = 2*1000 
elif numberofscoops == 3:
    scoop_price = 3*1000
elif numberofscoops == 4:
    scoop_price = 4*1000
else:
    print("Request Out of range") 
print(f"Price of Scoops = {scoop_price}")

print('''\tOptional Topping\tUGX
      1. Flake\t\t\t  400
      2. Chocolate sprinkle\t300
      3. Straw Berry Coulis\t600
''')
flake = input("Would you like to add a flake to your ice cream(yes or no): ")
chocolatesprinkle = input("Would you also like some chocolate sprinkle(yes or no): ")  
strawberry = input("Would you also like to add a straw berry(yes or no): ")

topping =  ""
if flake == "yes":
    topping == "Flake"
    toppings_price1 = 400
else:
    toppings_price1 = 0    
if chocolatesprinkle == "yes":
    topping == "Chocolate Sprinkle"
    toppings_price2 = 300
else:
    toppings_price2 = 0
if strawberry == "yes":
    topping == "Straw Berry Coulis"
    toppings_price3 = 600
else:
    toppings_price3 = 0
optionaltopping = toppings_price1 + toppings_price2 + toppings_price3         
print(f"Optional Topping price = {optionaltopping}")
icecream_cost = containerprice + scoop_price + optionaltopping
print(f"Your Ice cream Cost is : {icecream_cost}")     

