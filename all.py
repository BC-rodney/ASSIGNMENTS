restaurant = []

details = {
        "number": "001",
        "name":"JAVAS RESTAURANT",
        "address":"KAWEMPE, Bombo rd.",
        "contact person":"TWAHA",
        "contact":"0758102369",
        "opening hour":"06:00 am",
        "closing hour":"10:00 pm"
    }
restaurant.append(details)

#while True:
    #meal_no = input("Enter meal number or 'Q' to quit: ")
    #if meal_no.upper()=='Q':
        #break

meals = [
    {
        "meal no": "01",
        "meal details":["matooke","rice","meat"],
        "price": "12000",
        "status":"available"
    },
      {
        "meal no": "02",
        "meal details":["posho","beans","nakati"],
        "price": "5000",
        "status":"available"
    },
      {
        "meal no": "03",
        "meal details":["chicken","pilao","greans"],
        "price": "18000",
        "status":"available"
    },
      {
        "meal no": "04",
        "meal details":["pilao","Beef","greans"],
        "price": "20000",
        "status":"available"
    },
      {
        "meal no": "05",
        "meal details":["chips","chicken","salads"],
        "price": "25000",
        "status":"not available"
    }
]


def display_restaurant_details():
    for detail in restaurant:
        print(f"\n=====JAVA RESTAURANT DETAILS=====\n")
        print(f'No. :\t\t\t{details.get("number")}\nName :\t\t\t{details.get("name")}\nAddress :\t\t{details.get("address")}\nContact person : \t{details.get("contact person")}\nContact :\t\t{details.get("contact")}\nOpening Hours :\t\t{details.get("opening hour")}\nClosing Hour :\t\t{details.get("closing hour")}')

meal_details = [] 
for meal in meals:
   #for dish in meal["meal details"]:
    meal_details.append(meal["meal details"])
#print(meal_details)  

def display_menu():
    mealnums = ['01','02','03','04','05']
    print("\n\t\t*****MENU DETAILS*****\nMEAL NO.\t\tDISH\t\t\t\tPRICE\n")
    index = 0
    for meal in meals:
       output = f'{mealnums[index]}\t\t{meal_details[index]}\t\t'
       
       for i in meal["price"]:
          output += f'{i}'
            #for prices in meals:
                #output += f'{prices.get("price")})'
                
       index += 1
       print(output)    


print(display_menu())   
'''meal_details = []

    for i in range(4):
        dish = input("Enter Food: ")
        meal_details.append(dish)
    drink = input("Enter Drink: ")
    meal_details.append(drink)
    price = int(input("PRICE = "))
    status = input("STATUS: ")

    mealdict = {
        "meal number": meal_no,
        "meal details":meal_details,
        "price":price,
        "status":status
    }
    meals.append(mealdict)'''