"""
Wrote by Yokoo-arch 2023 (https://github.com/Yokoo-arch).
Github repository: https://github.com/Yokoo-arch/PyValAccountManager.
If you have any issues, please feel free to open an issue on the Github repository.
"""

#   Imports
import shutil
import app
import utility.mock as mock
import utility.db as DBUtility
import getch

#   Utility functions
def get_terminal_size():
    try:
        columns, lines = shutil.get_terminal_size()
        return columns, lines
    except Exception:
        return 80, 24  # Default values if unable to determine terminal size

def get_terminal_width():
    try:
        columns, _ = shutil.get_terminal_size()
        return columns
    except Exception:
        return 80  # Default value if unable to determine terminal size


def scale_ascii_art(ascii_art):
    terminal_width, _ = get_terminal_size()
    original_lines = ascii_art.split('\n')

    # Calculate the scaling factor
    scaling_factor = min(1.0, terminal_width / max(len(line) for line in original_lines))

    # Scale each line
    scaled_lines = [line[:int(len(line) * scaling_factor)] for line in original_lines]

    return '\n'.join(scaled_lines)

def center_text(text):
    terminal_width, _ = shutil.get_terminal_size()

    # Calculate left padding
    left_padding = (terminal_width - len(text)) // 2

    # Add left padding and print the centered text
    centered_text = ' ' * left_padding + text
    return centered_text

def center_ascii_art(ascii_art):
    terminal_width = get_terminal_width()

    # Calculate left padding
    left_padding = (terminal_width - max(len(line) for line in ascii_art.split('\n'))) // 2

    # Add left padding and print the centered ASCII art
    centered_ascii_art = '\n'.join(' ' * left_padding + line for line in ascii_art.split('\n'))
    return centered_ascii_art

def print_title(ascii_art:str) -> None:
    print(center_ascii_art(ascii_art=ascii_art))
    print(center_text("(Valorant Account Manager)"))

#   Constants
ascii_art = """
 _   _   ___  ___  ___
| | | | / _ \ |  \/  |
| | | |/ /_\ \| .  . |
| | | ||  _  || |\/| |
\ \_/ /| | | || |  | |
 \___/ \_| |_/\_|  |_/
"""

def print_menu():
    print("Main Menu:")
    print("(1) Create account")
    print("(2) Delete account")
    print("(3) List accounts")
    print("(4) List accounts of a certain rank")
    print("(5) Add accounts from a file")
    print("(6) Exit")

def handle_menu_selection(selection, App:app.App):
    if selection == "1":
        username = input("\nEnter the username of the account: ")
        password = input("Enter the password of the account: ")
        rank = input("Enter the rank (not the division) of the account (e.g. Gold): ")
        division = input("Enter the division of the account (e.g. 3)")
        ign = input("Enter the IGN (In Game Name) of the account: ")

        App.add_account(username, password, rank, division, ign)
        print("\nOne account has been added.")

    elif selection == "2":
        username = input("\nEnter the username of the account: ")
        
        App.remove_account(username)
        print("\nThe selected account has been removed.")

    elif selection == "3":
        account_list = App.list_account()
        if len(account_list) > 0:
            print("\nList of accounts:")
            for account in account_list:
                print(f"Username: {account['username']}, Rank: {account['rank']}, Division: {account['division']}, IGN: {account['ign']}, Password: {account['password']}")
        else:
            print("\nThere are no accounts to display.")
        
    elif selection == "4":
        rank = input("\nEnter the rank you wanna search for: ")
        account_list = App.list_account_rank(rank)
        if len(account_list) > 0:
            print("\nList of accounts:")
            for account in account_list:
                print(f"Username: {account['username']}, Rank: {account['rank']}, Division: {account['division']}, IGN: {account['ign']}, Password: {account['password']}")
        else:
            print("\nThere are no accounts to display.")

    elif selection == "5":
        filename = input("Enter the location of the file (e.g. data/accounts.txt): ")
        App.add_accounts_from_file(filename)

        print("\nAdded accounts.")
    
    elif selection == "6":
        # Exit the app
        print("Goodbye!")
        exit()
    else:
        print("\nInvalid selection. Please try again.")

def main():
    DBUtil = DBUtility.DataBaseUtility(dev_mode=False)
    App =app.App(dev_mode=False, DBUtil=DBUtil)

    DBUtil.empty_db()

    print_title(ascii_art=ascii_art)
    while True:
        print_menu()
        selection = input("Enter your selection: ").lower()
        handle_menu_selection(selection, App=App)
        input("\nPress ENTER to continue...")
        print("\n\n\n")

if __name__ == "__main__":
    main()