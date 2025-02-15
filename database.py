import os
import shelve
from prettytable import PrettyTable

class Pswddb:
    def __init__(self):
        # Define the database file path
        self.FILE = "pswdDB/db"

    def create_db(self):
        # Prompt the user for a name to create a new database
        print("Please enter your name while we create a new database for you!")
        while True:
            name = input("Name : ")
            
            # Ensure the name is not empty or only spaces
            if name.isspace() or name == "":
                print("Try again!")
            else:
                name.capitalize()  # Capitalize the name
                break
        
        # Create the directory for the database if it does not exist
        os.mkdir("pswdDB")
        
        # Open the database and initialize with user name and an empty password dictionary
        with shelve.open(self.FILE) as db:
            db["name"] = name
            db["passwords"] = {}

    def load_db(self):
        # Check if the database directory exists; if not, create a new database
        if not os.path.exists("pswdDB"):
            self.create_db()
        
        # Open the database and load the stored name and passwords
        with shelve.open(self.FILE) as db:
            name = db["name"]
            print(f"\n == Welcome {name} == \n")
            passwords = db["passwords"]
        return name, passwords

    def undo(self, passwords):
        # Remove the most recently added password entry
        with shelve.open(self.FILE) as db:
            passwords.popitem()  # Remove the last added entry

    def save(self, passwords):
        # Save the updated passwords dictionary back to the database
        with shelve.open(self.FILE) as db:
            db["passwords"] = passwords

    def clear_db(self):
        # Clear all stored passwords in the database
        with shelve.open(self.FILE) as db:
            db["passwords"] = {}  # Reset passwords dictionary
        print("All passwords cleared")
        exit()

    def show_pretty(self):
        # Load user name and passwords from the database
        name, passwords = self.load_db()

        # Create a formatted table to display stored passwords
        table = PrettyTable(["DOMAIN", "P.WORD"])
        table.min_table_width = 40
        table.max_table_width = 41
        table.align = 'l'  # Left-align text in table

        # Populate the table with stored passwords
        for domain, pswd in passwords.items():
            table.add_row([domain, pswd], divider=True)
        
        print(table)  # Display the formatted table

# pswd.py