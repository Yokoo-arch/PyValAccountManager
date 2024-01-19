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
        ranks = {
            "Iron":[1,2,3],
            "Bronze":[1,2,3],
            "Silver":[1,2,3],
            "Gold":[1,2,3],
            "Platinum":[1,2,3],
            "Diamond":[1,2,3],
            "Ascendant":[1,2,3],
            "Immortal":[1,2,3],
            "Radiant":[1]
        }
    
        rank = random.choice(list(ranks))
        subrank = random.choice(list(ranks[str(rank)]))
        if rank=="Radiant":
            return rank
        else:
            return f"{rank} {subrank}"
    
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