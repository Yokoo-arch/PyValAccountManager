"""
Wrote by Yokoo-arch 2023 (https://github.com/Yokoo-arch).
Github repository: https://github.com/Yokoo-arch/PyValAccountManager.
If you have any issues, please feel free to open an issue on the Github repository.
"""

# Imports
import app
import utility.mock as mock
import utility.db as DBUtility

# Main
DBUtil = DBUtility.DataBaseUtility(dev_mode=True)
App =app.App(dev_mode=True, DBUtil=DBUtil)

