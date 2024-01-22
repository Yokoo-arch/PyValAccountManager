"""
Module for the App class.
"""

from utility.log_config import logger
from utility.db import DataBaseUtility

class App:
    """
    Class for managing accounts and interacting with the database.
    """

    def __init__(self, dev_mode: bool, db_util: DataBaseUtility) -> None:
        """
        Initialize a new instance of the App class.

        Args:
            dev_mode (bool): Enable or disable development mode.
            db_util (DataBaseUtility): An instance of the DataBaseUtility class.
        """
        self.dev_mode = dev_mode
        self.DBUtil = db_util

        if not self.dev_mode:
            logger.error("Dev mode isn't enabled, so you don't have access to extensive debugging.")

    def add_accounts_from_file(self, filename: str) -> None:
        """
        Add accounts to the database from a file.

        The file should have one account per line, with each part of the account
        separated by a colon (e.g. "username:password:rank:division:ign").

        Args:
            filename (str): The name of the file to read from.

        Returns:
            None
        """
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(":")
                if len(parts) == 5:
                    self.add_account(*parts)
                else:
                    logger.warning(f"Ignoring line with incorrect number of parts: {line}")

    def add_account(self, username: str, password: str, rank: str, division: str, ign: str) -> None:
        """
        Add a new account to the account manager.
        """
        document = self.DBUtil.__generate_document__([username, password, rank, division, ign])
        self.DBUtil.push_documents([document])

    def remove_account(self, username: str) -> bool:
        """
        Remove an account from the database.

        Args:
            username (str): The username of the account to remove.

        Returns:
            bool: True if the account was removed, False otherwise.
        """
        try:
            count = self.DBUtil.collection.count_documents({"username": username})
            if count > 0:
                if count > 1:
                    self.DBUtil.collection.delete_many({"username": username})
                else:
                    self.DBUtil.collection.delete_one({"username": username})
                return True
            else:
                logger.warning(f"No account found with username '{username}'")
        except Exception as e:
            logger.error("An error occurred while trying to get the database.")
            print(e)

        return False

    def list_accounts(self) -> list:
        """
        List all the accounts in the database.

        Returns:
            list: A list of account dictionaries.
        """
        accounts = []
        cursor = self.DBUtil.collection.find({})
        for document in cursor:
            accounts.append(document)

        return accounts

    def list_accounts_by_rank(self, rank: str) -> list:
        """
        List all the accounts that have a certain rank.

        Args:
            rank (str): The rank of the accounts to list.

        Returns:
            list: A list of account dictionaries.
        """
        accounts = []
        cursor = self.DBUtil.collection.find({"rank": rank})
        for document in cursor:
            accounts.append(document)

        return accounts

    def dev_log(self, msg: str) -> None:
        """
        Log specified message if dev mode is enabled.

        Args:
            msg (str): The message to log.

        Returns:
            None
        """
        if self.dev_mode:
            logger.debug(msg)