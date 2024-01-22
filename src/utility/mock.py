#   Imports
import string
import random
from utility.log_config import logger

class MockData:
    def __init__(self, dev_mode:bool=False, username_token_size:int=8, password_size:int=20) -> None:
        self.username_token_size = username_token_size
        self.username_base = "D01"
        self.dev_mode = dev_mode
        self.password_size = password_size

    def  generate_token(self, size:int) -> str:
        """
        Generate a token of a certain size

        Returns:
            str: token
        """
        characters = string.ascii_letters + string.digits
        token = ''.join(random.choice(characters) for _ in range(size))
        return token
    
    def generate_username(self) -> str:
        """
        Generate a random username

        Returns:
            str: username like username_base+token
        """
        username = f"{self.username_base}-{self.generate_token(self.username_token_size)}"
        self.dev_log(f"Username: {username}")
        return username
    
    def generate_password(self) -> str:
        """
        Generate a random password of a defined size

        Returns:
            str: password
        """
        password = self.generate_token(self.password_size)
        self.dev_log(f"Password: {password}")
        return password

    def generate_ign(self) -> str:
        """
        Generate a random IGN

        Returns:
            str: IGN
        """
        char_list = string.digits
        tag = ''.join(random.choice(char_list) for _ in range(4))
        username = f"D01#{tag}"
        self.dev_log(f"IGN: {username}")
        return username

    def genereate_rank(self) -> str:
        """
        Generate a random rank

        Returns:
            str: Rank
        """
        ranks = ["Iron", "Bronze", "Silver", "Gold", "Platinum", "Ascendant", "Immortal", "Radiant"]
    
        return random.choice(ranks)

    def generate_divison(self) -> str:
        """
        Genrate a random divison

        Returns:
            str: Division
        """
        return str(random.randint(1, 3))
    
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