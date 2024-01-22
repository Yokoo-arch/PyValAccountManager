#   Imports
from pymongo import database, collection
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from utility.log_config import logger
from utility.mock import MockData
import dotenv
import os

class DataBaseUtility:
    def __init__(self, dev_mode:bool=True) -> None:
        self.dev_mode = dev_mode
        dotenv.load_dotenv()
        self.uri = os.getenv("MONGODB_URI")
        self.dev_log(f"MongoDB URI: {self.uri}") #Need to remove this line (because of security issue, showing username + password for mongodb connection uri)
        self.db_client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.check_connection_to_db()
        self.logger = logger
        self.mock = MockData(dev_mode=False)
        self.db = self.get_database()
        self.collection = self.get_collection()

    def check_connection_to_db(self) -> bool:
        """
        Check the connection to the MongoDB database.
        """
        try:
            self.db_client.server_info()
            logger.info("Connected to MongoDB successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            return False
        
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
    
    def __generate_document__(self, datas:list|None, is_mock:bool=False) -> dict[str, str]:
        """
        Generate a document

        Args:
            is_mock (bool, optional): test datas? Defaults to False.
            datas (str, str, str, str, str, optional): datas needed to create a document (only for non mock document)

        Returns:
            dict[str, str]: the document
        """
        if is_mock == True:
            division = self.mock.generate_divison()
            rank = self.mock.genereate_rank()
            
            if rank.lower() == "randiant":
                division = None
            
            document = {
                "username":self.mock.generate_username(),
                "password":self.mock.generate_password(),
                "rank":rank.lower(),
                "division":division,
                "ign":self.mock.generate_ign(),
                "is_mock":is_mock
            }
        if is_mock == False:
            document = {
                "username":datas[0],
                "password":datas[1],
                "rank":datas[2],
                "division":datas[3],
                "ign":datas[4],
                "is_mock":is_mock
            }
        return document
        
    def push_mock_data(self, ammount:int) -> None:
        """
        Push a certain number of fake datas to the db

        Args:
            ammount (int): number of fake documents

        Returns:
            None: nothing
        """
        try:
            datas = []
            for _ in range(ammount):
                datas.append(self.__generate_document__(None, is_mock=True))
            self.collection.insert_many(datas)
            self.dev_log(f"Inserted {len(datas)} documents to {self.collection.name}")
        except Exception as e:
            self.logger.error("An error occured while trying to get the database.")
            print(e)
        return None
    
    def empty_db(self) -> None:
        """
        Empty the db (of all data, be carefull)

        Returns:
            None: nothing
        """ 
        try:
            self.collection.delete_many({})
        except Exception as e:
            self.logger.error("An error occured while trying to get the database.")
            print(e)
        return None
    
    def clear_mock_data(self) -> None:
        """
        Only clear the fake datas

        Returns:
            None: nothing
        """
        try:
            self.collection.delete_many({"is_mock":True})
        except Exception as e:
            self.logger.error("An error occured while trying to get the database.")
            print(e)
        return None
    
    def push_documents(self, documents:list) -> None:
        """
        Push real datas to the db

        Args:
            documents (list): the list of documents

        Returns:
            None: nothing
        """
        try:
            self.collection.insert_many(documents)
            self.dev_log(f"Inserted {len(documents)} documents to {self.collection.name}")
        except Exception as e:
            self.logger.error("An error occured while trying to get the database.")
            print(e)
        return None