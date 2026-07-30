# database.py

import json
import os


class Database:
    def __init__(self):
        self.file_name = "users.json"

        # Create users.json if it doesn't exist
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w") as file:
                json.dump([], file, indent=4)

    def load_users(self):
        with open(self.file_name, "r") as file:
            return json.load(file)

    def save_users(self, users):
        with open(self.file_name, "w") as file:
            json.dump(users, file, indent=4)

    # -----------------------------
    # CREATE NEW ACCOUNT
    # -----------------------------
    def create_account(self, name, card_number, pin, balance):
        users = self.load_users()

        # Duplicate card number check
        for user in users:
            if user["card_number"] == card_number:
                return False

        new_user = {
            "name": name,
            "card_number": card_number,
            "pin": pin,
            "balance": balance,
            "transactions": []
        }

        users.append(new_user)
        self.save_users(users)

        return True

    # -----------------------------
    # LOGIN
    # -----------------------------
    def login(self, card_number, pin):
        users = self.load_users()

        for user in users:
            if user["card_number"] == card_number and user["pin"] == pin:
                return user

        return None

    # -----------------------------
    # UPDATE ACCOUNT
    # -----------------------------
    def update_account(self, updated_user):
        users = self.load_users()

        for i, user in enumerate(users):
            if user["card_number"] == updated_user["card_number"]:
                users[i] = updated_user
                break

        self.save_users(users)