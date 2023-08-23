"""
Wrote by Yokoo-arch 2023 (https://github.com/Yokoo-arch).
Github repository: https://github.com/Yokoo-arch/PyValAccountManager.
If you have any issues, please feel free to open an issue on the Github repository.
"""

# Imports
from enum import Enum, auto

class LogLevel(Enum):
    """
    Log level enum.
    """
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()