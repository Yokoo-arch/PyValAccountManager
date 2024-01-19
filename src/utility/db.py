#   Imports
from pymongo import mongo_client, database, collection
from utility.log_config import logger
from utility.mock import MockData

class DataBaseUtility:
    def __init__(self, mongo_client: mongo_client.MongoClient, dev_mode:bool=True) -> None:
        self.db_client = mongo_client
        self.logger = logger
        self.dev_mode = dev_mode
        self.mock = MockData(dev_mode=False)
        self.db = self.get_database()
        self.collection = self.get_collection()

    def get_database(self) -> database.Database|None:
        """
        Connect to the database table

        Returns:
            database.Database|None: Either none (if an error occured) or the db class
        """
        try:
            db = self.db_client["ValorantAccountManager"]
            self.dev_log("Succes, connected to the db table")
            return db
        except Exception as e:
            self.logger.error("An error occured while trying to get the database.")
            print(e)
            return None

    def get_collection(self) -> collection.Collection|None:
        """
        Connect to the collection

        Returns:
            collection.Collection|None: Either none (if an error occured) or the collection class
        """
        try:
            collection = self.get_database()["Accounts"]
            self.dev_log("Succes, connected to the collection")
            return collection
        except Exception as e:
            self.logger.error("An error occured while trying to get the database.")
            print(e)
            return None
    
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
    
    def __generate_document__(self, is_mock:bool=False) -> dict[str, str]:
        document = {
            "username":self.mock.generate_username(),
            "password":self.mock.generate_password(),
            "rank":self.mock.genereate_rank(),
            "ign":self.mock.generate_ign(),
            "is_mock":is_mock
        }

        return document
        
    def push_mock_data(self, ammount:int) -> None:
        try:
            datas = []
            for _ in range(ammount):
                datas.append(self.__generate_document__(is_mock=True))
            self.collection.insert_many(datas)
            self.dev_log(f"Inserted {len(datas)} documents to {self.collection.name}")
        except Exception as e:
            self.logger.error("An error occured while trying to get the database.")
            print(e)
        return None
    
    def empty_db(self) -> None:
        try:
            self.collection.delete_many({})
        except Exception as e:
            self.logger.error("An error occured while trying to get the database.")
            print(e)
        return None
    
    def clear_mock_data(self) -> None:
        try:
            self.collection.delete_many({"is_mock":True})
        except Exception as e:
            self.logger.error("An error occured while trying to get the database.")
            print(e)
        return None