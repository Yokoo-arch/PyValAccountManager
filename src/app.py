# Imports
import argparse
import dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from utility.log_config import logger
from utility.log_level import LogLevel

class App:
    def __init__(self, dev_mode:bool) -> None:
        """
        App class initialization function.
        """
        self.dev_mode = dev_mode #Extensive debuging information
        
        if self.dev_mode == False:
            logger.error("Dev mode isn't enabled, so you don't have acces to extensive debugging.")
        
        # Loading .env configuration file
        dotenv.load_dotenv()
        self.uri = os.getenv("MONGODB_URI")
        self.dev_log(f"MongoDB URI: {self.uri}") #Need to remove this line (because of security issue, showing username + password for mongodb connection uri)
        self.mongoClient = MongoClient(self.uri, server_api=ServerApi('1'))
        self.check_connection_to_db()
    
    def check_connection_to_db(self) -> bool:
        """
        Check the connection to the MongoDB database.
        """
        try:
            self.mongoClient.server_info()
            logger.info("Connected to MongoDB successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            return False
    
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
    
    def add_account(self) -> None:
        """
        Add a new account to the account manager.
        """
        pass

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