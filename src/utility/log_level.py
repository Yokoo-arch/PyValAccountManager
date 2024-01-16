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