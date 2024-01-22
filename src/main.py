"""
Valorant Account Manager========================

A simple console application to manage Valorant accounts.

Written by Yok-arch 2023 (https://github.com/Yokoo-arch).
Github repository: https://github.com/Yokoo-arch/PyValAccountManager.
If you have any issues, please feel free to open an issue on the Github repository.
"""

import shutil
from app import App 
import utility.mock as mock
import utility.db as db_utility
import getch

# Utility functions
def get_terminal_size():
    """Get terminal size and return columns and lines."""
    try:
        columns, lines = shutil.get_terminal_size()
        return columns, lines
    except Exception:
        return 80, 24  # Default values if unable to determine terminal size

def get_terminal_width():
    """Get terminal width and return columns."""
    try:
        columns, _ = shutil.get_terminal_size()
        return columns
    except Exception:
        return 80  # Default value if unable to determine terminal size

def scale_ascii_art(ascii_art):
    """Scale ASCII art to fit the terminal width."""
    terminal_width, _ = get_terminal_size()
    original_lines = ascii_art.split('\n')

    scaling_factor = min(1.0, terminal_width / max(len(line) for line in original_lines))
    scaled_lines = [line[:int(len(line) * scaling_factor)] for line in original_lines]

    return '\n'.join(scaled_lines)

def center_text(text):
    """Center text based on the terminal width."""
    terminal_width, _ = shutil.get_terminal_size()
    left_padding = (terminal_width - len(text)) // 2
    return ' ' * left_padding + text

def center_ascii_art(ascii_art):
    """Center ASCII art based on the terminal width."""
    terminal_width = get_terminal_width()
    left_padding = (terminal_width - max(len(line) for line in ascii_art.split('\n'))) // 2
    return '\n'.join(' ' * left_padding + line for line in ascii_art.split('\n'))

def print_title(ascii_art):
    """Print the title with centered ASCII art."""
    print(center_ascii_art(ascii_art=ascii_art))
    print(center_text("(Valorant Account Manager)"))

# Constants
ASCII_ART = """
 _   _   ___  ___  ___
| | | | / _ \ |  \/  |
| | | |/ /_\ | .  . |
| | | ||  _  || |\/| |
\ \_/ /| | | || |  | |
 \___/ \_| |_/\_|  |_/
"""

def print_menu():
    """Print the main menu."""
    print("Main Menu:")
    print("(1) Create account")
    print("(2) Delete account")
    print("(3) List accounts")
    print("(4) List accounts of a certain rank")
    print("(5) Add accounts from a file")
    print("(6) Exit")

def handle_menu_selection(selection, app):
    """Handle the user's menu selection."""
    if selection == "1":
        add_account(app)

    elif selection == "2":
        delete_account(app)

    elif selection == "3":
        list_accounts(app)

    elif selection == "4":
        list_accounts_by_rank(app)

    elif selection == "5":
        add_accounts_from_file(app)

    elif selection == "6":
        print("Goodbye!")
        exit()

    else:
        print("\nInvalid selection. Please try again.")

def add_account(app):
    """
    Add an account to the database.

    Args:
        app (App): The App instance to use for adding the account.

    Returns:
        None
    """
    username = input("\nEnter the username of the account: ")
    password = input("Enter the password of the account: ")
    rank = input("Enter the rank (not the division) of the account (e.g. Gold): ")
    division = input("Enter the division of the account (e.g. 3)")
    ign = input("Enter the IGN (In Game Name) of the account: ")

    app.add_account(username, password, rank, division, ign)
    print("\nOne account has been added.")

def delete_account(app):
    """
    Delete an account from the database.

    Args:
        app (App): The App instance to use for deleting the account.

    Returns:
        None
    """
    username = input("\nEnter the username of the account: ")

    app.remove_account(username)
    print("\nThe selected account has been removed.")

def list_accounts(app):
    """
    List all accounts in the database.

    Args:
        app (App): The App instance to use for listing the accounts.

    Returns:
        None
    """
    account_list = app.list_accounts()
    if len(account_list) > 0:
        print("\nList of accounts:")
        for account in account_list:
            print(f"Username: {account['username']}, Rank: {account['rank']}, Division: {account['division']}, IGN: {account['ign']}, Password: {account['password']}")
    else:
        print("\nThere are no accounts to display.")

def list_accounts_by_rank(app):
    """
    List all accounts in the database with a certain rank.

    Args:
        app (App): The App instance to use for listing the accounts.

    Returns:
        None
    """
    rank = input("\nEnter the rank you wanna search for: ")
    account_list = app.list_accounts_by_rank(rank)
    if len(account_list) > 0:
        print("\nList of accounts:")
        for account in account_list:
            print(f"Username: {account['username']}, Rank: {account['rank']}, Division: {account['division']}, IGN: {account['ign']}, Password: {account['password']}")
    else:
        print("\nThere are no accounts to display.")

def add_accounts_from_file(app):
    """
    Add accounts to the database from a file.

    The file should have one account per line, with each part of the account
    separated by a colon (e.g. "username:password:rank:division:ign").

    Args:
        app (App): The App instance to use for adding the accounts.
        filename (str): The name of the file to read from.

    Returns:
        None
    """
    filename = input("Enter the location of the file (e.g. data/accounts.txt): ")
    try:
        app.add_accounts_from_file(filename)
        print("\nAdded accounts.")
    except:
        print("\nAn errror occured.")


def main():
    """Run the main application."""
    db_util = db_utility.DataBaseUtility(dev_mode=False)
    app = App(dev_mode=False, db_util=db_util)

    print_title(ascii_art=ASCII_ART)
    while True:
        print_menu()
        selection = input("Enter your selection: ").lower()
        handle_menu_selection(selection, app)
        input("\nPress ENTER to continue...")
        print("\n\n\n")

if __name__ == "__main__":
    main()