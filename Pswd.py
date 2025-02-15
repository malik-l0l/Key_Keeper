import time
from database import Pswddb

def recieve_password():
    # Prompt user for a password until a valid input is given
    while True:
        password = input("Pswd :")
        if password != "" and not password.isspace():
            break  # Exit loop if a valid password is entered
    return password

def main():
    db = Pswddb()
    name, passwords = db.load_db()

    while True:
        domain_name = input("Domain :")
        
        if domain_name == "" or domain_name.isspace():
            pass  # Ignore empty inputs
        
        elif domain_name == "clear":
            # Ask for confirmation before clearing database
            x = input("Are you sure to clear database ? (y/n)").lower()
            if x != "n":
                db.clear_db()
        
        elif domain_name == "undo":
            # Undo the last stored password
            db.undo(passwords)
        
        elif domain_name.lower() == "help":
            # Display available commands in a structured format
            print("\nAvailable commands:")
            print("  clear   - Clears all stored passwords")
            print("  u       - Undo the last password entry")
            print("  help    - Show this help menu")
            print("  q       - Quit the program")
            print("  [HHMM]  - Show stored passwords (Enter current time in HHMM format)")
            print("  [name]  - Store a new password for a domain\n")

            print("just type in the domain name (for_eg: gmail.com), hit enter, then type the password (for_eg: simple@123), hit enter!!\n")
        
        elif domain_name == time.strftime("%H%M", time.localtime()) and domain_name.isdigit():
            # Show stored passwords if user inputs current time in HHMM format
            db.show_pretty()
        
        elif len(domain_name) < 6 and domain_name.isdigit():
            print("Wrong key!\n")  # Prevent short numeric inputs
        
        elif domain_name == "q":
            # Exit the program
            print("-- Bei --".center(41))
            exit()
        
        else:
            # Store a new password for the given domain
            password = recieve_password()
            passwords[domain_name] = password
            print("\n-- PASSWORD SAVED --\n")
        
        # Save the updated passwords dictionary
        db.save(passwords)

# Run the main function
main()
