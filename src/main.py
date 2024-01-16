"""
Wrote by Yokoo-arch 2023 (https://github.com/Yokoo-arch).
Github repository: https://github.com/Yokoo-arch/PyValAccountManager.
If you have any issues, please feel free to open an issue on the Github repository.
"""

# Imports
import app
import utility.mock as mock

# Main
App =app.App(dev_mode=True)
Mock = mock.MockData(dev_mode=True)

for _ in range(5):
    Mock.generate_username()
    Mock.generate_password()