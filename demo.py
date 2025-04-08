import pyodbc

for driver in pyodbc.drivers():
    print(driver)

import os
from dotenv import load_dotenv
load_dotenv()
print(os.environ.get('DATABASE_PASSWORD'))