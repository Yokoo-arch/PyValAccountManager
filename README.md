 # PyValAccountManager

PyValAccountManager is a Python application that allows users to manage their Valorant accounts. It includes features such as adding, deleting, and listing accounts, as well as filtering accounts by rank.

## Installation

To install PyValAccountManager, clone the repository and install the required dependencies:

```
git clone https://github.com/Yokoo-arch/PyValAccountManager.git
cd PyValAccountManager
pip install -r requirements.txt
```

## Usage

To use PyValAccountManager, run the following command:

```
python src/main.py
```

This will launch the main menu, which provides the following options:

1. Create account
2. Delete account
3. List accounts
4. List accounts of a certain rank
5. Add accounts from a file
6. Exit

To create an account, select option 1 and enter the following information:

* Username
* Password
* Rank
* Division
* IGN (In-Game Name)

To delete an account, select option 2 and enter the username of the account you want to delete.

To list all accounts, select option 3.

To list accounts of a certain rank, select option 4 and enter the rank you want to search for.

To add accounts from a file, select option 5 and enter the location of the file. The file should contain one account per line, with each part of the account separated by a colon (e.g. "username:password:rank:division:ign").

To exit the application, select option 6.

## Code Overview

The PyValAccountManager application consists of the following files:

* `app.py`: This file contains the main application logic.
* `main.py`: This file is the entry point of the application.
* `utility/db.py`: This file contains the code for interacting with the database.
* `utility/log_config.py`: This file configures the logging system.
* `utility/log_level.py`: This file defines the log levels used by the application.
* `utility/mock.py`: This file contains the code for generating mock data.
