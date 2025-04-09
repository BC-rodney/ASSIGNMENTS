#A console application for new line technologies
print("\nChoose Option\n1. Transfer Money\n2. Withdraw Money\n3. Deposit Money\n4. Account Balance")

my_pin = "1234"
account_balance = 10000
transfer_amount = 0
option = int(input("Enter Option :"))
if option == 1:
    phone_number = input("Please enter Receiver Phone Number: ")
    pin = input("Enter PIN: ")
    if pin != my_pin:
        print("Wrong PIN")
    else:
        transfer_amount = int(input("Enter Transfer Amount: "))
        if account_balance > (transfer_amount + (0.05 * account_balance)):
            print("Transaction Successful")    
        else:
            print("Insufficient Balance")
elif option == 2:
    pin = input("Enter PIN: ")
    withdraw_amount = int(input("Enter Withdraw Amount: "))
    if account_balance > (withdraw_amount + (0.05 * account_balance)):
        print("Withdraw Successful")
    else:
        print("Insufficient Balance")
elif option == 3:
    deposit_amount = input("Enter Deposit Amount: ")
    if deposit_amount > 500:
        print("Deposit Successful")
        account_balance += deposit_amount
    else:
        print("Insufficient Amount")
else:
    
    print(f"Account Balance = {account_balance}")
