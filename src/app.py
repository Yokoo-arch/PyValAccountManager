# Imports
from utility.log_config import logger
from utility.db import DataBaseUtility
class App:
    def __init__(self, dev_mode:bool, DBUtil:DataBaseUtility) -> None:
        """
        App class initialization function.
        """
        self.dev_mode = dev_mode #Extensive debuging information
        
        if self.dev_mode == False:
            logger.error("Dev mode isn't enabled, so you don't have acces to extensive debugging.")
        
        self.DBUtil = DBUtil
    
    def add_accounts_from_file(self, filename:str) -> None:
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
                    self.add_account(parts[0], parts[1], parts[2], parts[3], parts[4])
                else:
                    logger.warning(f"Ignoring line with incorrect number of parts: {line}")
                    
    def add_account(self, username:str, password:str, rank:str, divison:str, ign: str) -> None:
        """
        Add a new account to the account manager.
        """
        doc = self.DBUtil.__generate_document__([username, password, rank, divison, ign])
        self.DBUtil.push_documents([doc])

    def remove_account(self, username:str) -> bool:
        """
        Remove an account from the db

        Args:
            username (str): the filter

        Returns:
            bool:
        """
        try:
            if  self.DBUtil.collection.count_documents({"username": username}) > 1:
                self.DBUtil.collection.delete_many({"username": username})
            else:
                self.DBUtil.collection.delete_one({"username": username})
                
            return True
        except Exception as e:
            self.logger.error("An error occured while trying to get the database.")
            print(e)
            return False
    
    def list_account(self) -> list:
        """
        List all the accounts in the db

        Returns:
            list: accounts list
        """
        accounts = []
        cursor = self.DBUtil.collection.find({})
        for document in cursor:
            accounts.append(document)
        
        return accounts

    def list_account_rank(self, rank:str) -> list:
        """
        List all the accounts that have a certain rank

        Args:
            rank (str): The rank

        Returns:
            list: accounts list
        """
        accounts = []
        cursor = self.DBUtil.collection.find({"rank": rank})
        for document in cursor:
            accounts.append(document)
        
        return accounts
    def dev_log(self, msg: str) -> None:
            """
            Log specified message if dev mode is enabled.

            Parameters:
            - msg (str): The message to log.

            Returns:
            None
            """
            if self.dev_mode:
                logger.debug(msg)