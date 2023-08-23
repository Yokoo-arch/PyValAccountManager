"""
Wrote by Yokoo-arch 2023 (https://github.com/Yokoo-arch).
Github repository: https://github.com/Yokoo-arch/PyValAccountManager.
If you have any issues, please feel free to open an issue on the Github repository.
"""

# Imports
import argparse
import dotenv
import pymongo
import os
import getpass
from utility.log_config import logger
from utility.log_level import LogLevel

class app:
    def __init__(self, dev:bool) -> None:
        """
        App class initialization function.
        """
        self.dev = dev #Extensive debuging information
        dotenv.load_dotenv()
        self.uri = os.getenv("MONGODB_URI")
        self.dev_mode_log(f"MongoDB URI: {self.uri}", LogLevel.DEBUG) #Need to remove this line (because of security issue, showing username + password for mongodb connection uri)
    
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

    def dev_mode_log(self, message:str, log_level:LogLevel = LogLevel.INFO) -> None:
        """
        Extensive debugging information if dev mode is enabled.
        """
        if self.dev:
            match log_level:
                case LogLevel.DEBUG:
                    logger.debug(message)
                case LogLevel.INFO:
                    logger.info(message)
                case LogLevel.WARNING:
                    logger.warning(message)
                case LogLevel.ERROR:
                    logger.error(message)
                case LogLevel.CRITICAL:
                    logger.critical(message)
        else:
            logger.error("Dev mode isn't enabled, so you don't have acces to extensive debugging.")