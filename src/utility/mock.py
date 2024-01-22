"""
Module for generating mock data.
"""

import string
import random
from utility.log_config import logger  # type: ignore

class MockData:
    """
    Class for generating mock data.
    """

    def __init__(
        self,
        dev_mode: bool = False,
        username_token_size: int = 8,
        password_size: int = 20,
    ) -> None:
        """
        Initialize a new instance of the MockData class.

        Args:
            dev_mode (bool, optional): Enable or disable development mode. Defaults to False.
            username_token_size (int, optional): The size of the username token. Defaults to 8.
            password_size (int, optional): The size of the password. Defaults to 20.
        """
        self.username_token_size = username_token_size
        self.username_base = "D01"
        self.dev_mode = dev_mode
        self.password_size = password_size

    def generate_token(self, size: int) -> str:
        """
        Generate a token of a certain size.

        Args:
            size (int): The size of the token.

        Returns:
            str: The generated token.
        """
        characters = string.ascii_letters + string.digits
        token = "".join(random.choice(characters) for _ in range(size))
        return token

    def generate_username(self) -> str:
        """
        Generate a random username.

        Returns:
            str: The generated username.
        """
        username = f"{self.username_base}-{self.generate_token(self.username_token_size)}"
        self.dev_log(f"Username: {username}")
        return username

    def generate_password(self) -> str:
        """
        Generate a random password of a defined size.

        Returns:
            str: The generated password.
        """
        password = self.generate_token(self.password_size)
        self.dev_log(f"Password: {password}")
        return password

    def generate_ign(self) -> str:
        """
        Generate a random IGN.

        Returns:
            str: The generated IGN.
        """
        char_list = string.digits
        tag = "".join(random.choice(char_list) for _ in range(4))
        username = f"D01#{tag}"
        self.dev_log(f"IGN: {username}")
        return username

    def generate_rank(self) -> str:
        """
        Generate a random rank.

        Returns:
            str: The generated rank.
        """
        ranks = [
            "Iron",
            "Bronze",
            "Silver",
            "Gold",
            "Platinum",
            "Ascendant",
            "Immortal",
            "Radiant",
        ]
        return random.choice(ranks)

    def generate_division(self) -> str:
        """
        Generate a random division.

        Returns:
            str: The generated division.
        """
        return str(random.randint(1, 3))

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