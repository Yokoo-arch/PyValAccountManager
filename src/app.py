# Imports
import argparse
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
    
    def parse_args(self) -> argparse.Namespace:
        """
        Parse the CLI arguments.
        """
        argparser = argparse.ArgumentParser()
        
        argparser.add_argument("-a", "--add",
                               dest="add",
                               action="store_true",
                               help="Add a new account to the account manager.")
        argparser.add_argument("-r", "--remove",
                               dest="remove",
                               action="store_true",
                               help="Remove an existing account from the account manager.")
        argparser.add_argument("-l", "--list",
                               dest="list",
                               action="store_true",
                               help="List all accounts in the account manager.")
    
        self.options = argparser.parse_args()

        # Check if at least one mode option is provided
        if not any([self.options.add, self.options.remove, self.options.list]):
            argparser.error("Please provide at least one mode option. Type -h or --help for more information.")

        return self.options
    
    def add_account(self, username:str, password:str, rank:str, ign: str) -> None:
        """
        Add a new account to the account manager.
        """
        doc = self.DBUtil.__generate_document__([username, password, rank, ign])
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