# ATM-Simulation

A Python-based ATM Simulation System that allows users to create an account, securely log in using a card number and PIN, and perform essential banking operations through a command-line interface. User information and transaction history are stored permanently in a JSON file, making the application simple, interactive, and suitable for learning Python concepts.

## Features

1. Create a new ATM account
2. Secure login using Card Number and PIN
3. Maximum 3 login attempts
4. Duplicate card number validation
5. 4-digit PIN validation
6. Initial deposit during account creation
7. Check account balance
8. Deposit money
9. Withdraw money
10. Change ATM PIN
11. View Mini Statement with date & time
12. Permanent data storage using users.json
13. Logout and Exit options
14. Input validation and error handling

## Run the application using the following command:

python atm.py or py atm.py

## Main Menu
After running the program, the following menu appears:

            PYTHON ATM SIMULATION
==================================================

1. Create New Account
2. Login
3. Exit

==================================================
Enter your choice:

Option 1 – Create New Account

Creates a new ATM account by entering:

Full Name
10-digit Card Number
4-digit PIN
Confirm PIN
Initial Deposit
If all details are valid, the account is created successfully and stored in users.json.

Option 2 – Login

Log in using your registered Card Number and PIN.
After successful login, the ATM Menu is displayed.

Option 3 – Exit

Safely closes the application.

## ATM Menu

After successful login, the following menu appears:

                ATM MENU
==================================================

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Change PIN
5. Mini Statement
6. Logout
7. Exit

==================================================
Enter your choice:
Enter Account number:
Enter pin:

After check this
1. Check Balance
   
Displays the current account balance.

2. Deposit Money
   
Adds money to the user's account and updates the balance.

3. Withdraw Money
   
Withdraws money if sufficient balance is available.

4. Change PIN
   
Allows the user to change their 4-digit ATM PIN securely.

5. Mini Statement
   
Displays all transaction history along with date and time.

6. Logout
   
Logs out the current user and returns to the Main Menu.

7. Exit
   
Saves all data and exits the application
