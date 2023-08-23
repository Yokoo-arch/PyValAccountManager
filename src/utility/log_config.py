"""
Wrote by Yokoo-arch 2023 (https://github.com/Yokoo-arch).
Github repository: https://github.com/Yokoo-arch/PyValAccountManager.
If you have any issues, please feel free to open an issue on the Github repository.
"""

# Imports
from loguru import logger
import sys
import os
import dotenv

dotenv.load_dotenv()
log_file = os.getenv("LOG_FILE_BOOL").lower()

# Configure Loguru to write logs to the console and a file
logger.remove()
logger.add(sys.stderr, level="DEBUG")  # Write logs to console
if log_file=="true":
    logger.add("./log/output.log", rotation="500 MB", level="INFO")  # Write logs to a file