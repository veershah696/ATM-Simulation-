# transactions.py

from datetime import datetime


class TransactionManager:
    def __init__(self, transactions=None):
        if transactions is None:
            self.transactions = []
        else:
            self.transactions = transactions

    # Get current date & time
    def get_datetime(self):
        return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    # Add new transaction
    def add_transaction(self, transaction_type, amount=0):
        transaction = {
            "date": self.get_datetime(),
            "type": transaction_type,
            "amount": amount
        }

        self.transactions.append(transaction)

    # Return all transactions
    def get_transactions(self):
        return self.transactions

    # Display Mini Statement
    def display_transactions(self):
        print("\n" + "=" * 55)
        print("               MINI STATEMENT")
        print("=" * 55)

        if len(self.transactions) == 0:
            print("No Transactions Found.")
            return

        for transaction in self.transactions:

            print(f"Date   : {transaction['date']}")
            print(f"Type   : {transaction['type']}")

            if transaction["amount"] != 0:
                print(f"Amount : ₹{transaction['amount']}")

            print("-" * 55)