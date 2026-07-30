import json
import os
from datetime import datetime

DATABASE_FILE = "users.json"

# ================= LOAD USERS =================

def load_users():

    if not os.path.exists(DATABASE_FILE):
        return {}

    try:
        with open(DATABASE_FILE, "r") as file:
            users = json.load(file)

            if isinstance(users, dict):
                return users
            else:
                return {}

    except:
        return {}

# ================= SAVE USERS =================

def save_users(users):

    with open(DATABASE_FILE, "w") as file:
        json.dump(users, file, indent=4)


# ================= CREATE ACCOUNT =================
def create_account(users):

    print("\n===== CREATE ACCOUNT =====")
    name = input("Enter your name: ")
    account_number = input("Enter account number: ")

    if account_number in users:

        print("Account already exists!")

        return

    pin = input("Create 4 digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():

        print("Invalid PIN!")

        return

    users[account_number] = {

        "name": name,
        "pin": pin,
        "balance": 0,
        "transactions": []

    }


    save_users(users)

    print("\nAccount created successfully!")
    print("Account Number:", account_number)

    input("\nPress Enter to continue...")
    
# ================= LOGIN =================

def login(users):

    print("\n===== LOGIN =====")

    account_number = input("Enter account number: ")

    if account_number not in users:

        print("Account not found!")
        return None

    for attempt in range(3):

        pin = input("Enter PIN: ")

        if users[account_number]["pin"] == pin:

            print("\nLogin Successful")
            print("Welcome", users[account_number]["name"])

            return account_number

        else:

            print("Wrong PIN")

            print("Attempts left:", 2-attempt)

    print("Account locked!")

    return None

# ================= CHECK BALANCE =================

def check_balance(users, account):

    print("\n===== BALANCE =====")
    print("Current Balance: ₹", users[account]["balance"])
    input("\nPress Enter to continue...")

# ================= DEPOSIT =================

def deposit(users, account):

    print("\n===== DEPOSIT MONEY =====")

    amount = float(input("Enter amount: "))


    users[account]["balance"] += amount


    users[account]["transactions"].append(
        "Deposited ₹" + str(amount)
    )


    save_users(users)


    print("\nDeposit successful")
    print("Current Balance: ₹", users[account]["balance"])

    input("\nPress Enter to continue...")

# ================= WITHDRAW =================

def withdraw(users, account):

    print("\n===== WITHDRAW MONEY =====")

    amount = float(input("Enter amount: "))

    if amount > users[account]["balance"]:

        print("Insufficient balance")

        input("\nPress Enter to continue...")
        return

    users[account]["balance"] -= amount
    users[account]["transactions"].append(
        "Withdrawn ₹" + str(amount)
    )

    save_users(users)

    print("\nWithdrawal successful")
    print("Remaining Balance: ₹", users[account]["balance"])

    input("\nPress Enter to continue...")
# ================= CHANGE PIN =================

def change_pin(users, account):

    print("\n===== CHANGE PIN =====")


    old_pin = input("Enter old PIN: ")


    if old_pin != users[account]["pin"]:

        print("Wrong old PIN")

        input("\nPress Enter to continue...")
        return

    new_pin = input("Enter new 4 digit PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():

        print("Invalid PIN")

        input("\nPress Enter to continue...")
        return

    users[account]["pin"] = new_pin
    save_users(users)

    print("\nPIN changed successfully")
    input("\nPress Enter to continue...")

# ================= MINI STATEMENT =================

def mini_statement(users, account):

    print("\n===== MINI STATEMENT =====")
    transactions = users[account]["transactions"]

    if len(transactions) == 0:

        print("No transactions found")

    else:

        for transaction in transactions:

            print(transaction)

    input("\nPress Enter to continue...")

# ================= ATM MENU =================

def atm_menu(users, account):

    while True:

        print("\n======================")
        print("        ATM MENU")
        print("======================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Mini Statement")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == "1":

            check_balance(users, account)

        elif choice == "2":

            deposit(users, account)

        elif choice == "3":

            withdraw(users, account)

        elif choice == "4":

            change_pin(users, account)

        elif choice == "5":

            mini_statement(users, account)

        elif choice == "6":

            print("Logout successful")
            break

        else:

            print("Invalid choice")

# ================= MAIN =================

def main():

    users=load_users()
    while True:

        print("\n======================")
        print("    ATM SIMULATION")
        print("======================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice=input("Enter choice: ")

        if choice=="1":

            create_account(users)

        elif choice=="2":

            account=login(users)

            if account:

                atm_menu(users,account)

        elif choice=="3":

            print("Thank you!")

            break

        else:

            print("Invalid option")

if __name__=="__main__":

    main()