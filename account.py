# account.py

from transactions import TransactionManager


class Account:
    def __init__(self, user):
        self.user = user
        self.transaction_manager = TransactionManager(
            user.get("transactions", [])
        )

    # -------------------------
    # Check Balance
    # -------------------------
    def check_balance(self):
        return self.user["balance"]

    # -------------------------
    # Deposit Money
    # -------------------------
    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be greater than 0."

        self.user["balance"] += amount

        self.transaction_manager.add_transaction(
            "Deposit",
            amount
        )

        self.user["transactions"] = self.transaction_manager.get_transactions()

        return True, "Deposit Successful."

    # -------------------------
    # Withdraw Money
    # -------------------------
    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be greater than 0."

        if amount > self.user["balance"]:
            return False, "Insufficient Balance."

        self.user["balance"] -= amount

        self.transaction_manager.add_transaction(
            "Withdraw",
            amount
        )

        self.user["transactions"] = self.transaction_manager.get_transactions()

        return True, "Withdrawal Successful."

    # -------------------------
    # Change PIN
    # -------------------------
    def change_pin(self, old_pin, new_pin):

        if old_pin != self.user["pin"]:
            return False, "Current PIN is incorrect."

        if not new_pin.isdigit() or len(new_pin) != 4:
            return False, "PIN must be exactly 4 digits."

        self.user["pin"] = new_pin

        self.transaction_manager.add_transaction(
            "PIN Changed"
        )

        self.user["transactions"] = self.transaction_manager.get_transactions()

        return True, "PIN Changed Successfully."

    # -------------------------
    # Mini Statement
    # -------------------------
    def show_transactions(self):
        self.transaction_manager.display_transactions()

    # -------------------------
    # Return Updated User Data
    # -------------------------
    def get_user(self):
        self.user["transactions"] = self.transaction_manager.get_transactions()
        return self.user