import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

database_password = os.environ.get('DATABASE_PASSWORD')
suszi_login = 'stoszek'
server = 'morfeusz.wszib.edu.pl'

connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'Server={server};'
    f'DATABASE={suszi_login};'
    f'UID={suszi_login};'
    f'PWD={database_password};'
    'Encrypt=no'
)

connection = pyodbc.connect(connection_string)



