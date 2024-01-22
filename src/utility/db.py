"""
Module for the DataBaseUtility class.
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.collection import Collection
from pymongo.database import Database
from typing import List, Dict, Union
import dotenv
import os
from utility.log_config import logger
from utility.mock import MockData

class DataBaseUtility:
    """
    Class for managing database connections and operations.
    """

    def __init__(self, dev_mode: bool = True) -> None:
        """
        Initialize a new instance of the DataBaseUtility class.

        Args:
            dev_mode (bool): Enable or disable development mode.
        """
        self.dev_mode = dev_mode
        dotenv.load_dotenv()
        self.uri = os.getenv("MONGODB_URI")
        self.db_client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.check_connection_to_db()
        self.logger = logger
        self.mock = MockData(dev_mode=False)
        self.database = self.get_database()
        self.collection: Union[Collection, None] = self.get_collection()

    def check_connection_to_db(self) -> bool:
        """
        Check the connection to the MongoDB database.

        Returns:
            bool: True if connected, False otherwise.
        """
        try:
            self.db_client.server_info()
            logger.info("Connected to MongoDB successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            return False

    def get_database(self) -> Database:
        """
        Connect to the database.

        Returns:
            Database: The database object.
        """
        try:
            db = self.db_client["ValorantAccountManager"]
            return db
        except Exception as e:
            self.logger.error("An error occurred while trying to get the database.")
            print(e)
            return None

    def get_collection(self) -> Collection:
        """
        Connect to the collection.

        Returns:
            Collection: The collection object.
        """
        try:
            collection = self.get_database()["Accounts"]
            return collection
        except Exception as e:
            self.logger.error("An error occurred while trying to get the collection.")
            print(e)
            return None

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

    def __generate_document__(self, datas: List[str], is_mock: bool = False) -> Dict[str, str]:
        """
        Generate a document.

        Args:
            is_mock (bool, optional): Test datas? Defaults to False.
            datas (List[str]): Datas needed to create a document (only for non-mock documents).

        Returns:
            Dict[str, str]: The document.
        """
        if is_mock:
            division = self.mock.generate_division()
            rank = self.mock.generate_rank()

            if rank.lower() == "radiant":
                division = None

            document = {
                "username": self.mock.generate_username(),
                "password": self.mock.generate_password(),
                "rank": rank.lower(),
                "division": division,
                "ign": self.mock.generate_ign(),
                "is_mock": is_mock,
            }
        else:
            document = {
                "username": datas[0],
                "password": datas[1],
                "rank": datas[2],
                "division": datas[3],
                "ign": datas[4],
                "is_mock": is_mock,
            }

        return document

    def push_mock_data(self, ammount: int) -> None:
        """
        Push a certain number of fake datas to the db.

        Args:
            ammount (int): Number of fake documents.

        Returns:
            None
        """
        try:
            datas = [self.__generate_document__(None, is_mock=True) for _ in range(ammount)]
            self.collection.insert_many(datas)
            self.dev_log(f"Inserted {len(datas)} documents to {self.collection.name}")
        except Exception as e:
            self.logger.error("An error occurred while trying to push mock data.")
            print(e)
        return None

    def empty_db(self) -> None:
        """
        Empty the database (of all data, be careful).

        Returns:
            None
        """
        try:
            self.collection.delete_many({})
        except Exception as e:
            self.logger.error("An error occurred while trying to empty the database.")
            print(e)
        return None

    def clear_mock_data(self) -> None:
        """
        Only clear the fake datas.

        Returns:
            None
        """
        try:
            self.collection.delete_many({"is_mock": True})
        except Exception as e:
            self.logger.error("An error occurred while trying to clear mock data.")
            print(e)
        return None

    def push_documents(self, documents: List[Dict[str, str]]) -> None:
        """
        Push real datas to the db.

        Args:
            documents (List[Dict[str, str]]): The list of documents.

        Returns:
            None
        """
        try:
            self.collection.insert_many(documents)
            self.dev_log(f"Inserted {len(documents)} documents to {self.collection.name}")
        except Exception as e:
            self.logger.error("An error occurred while trying to push documents.")
            print(e)
        return None