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

#connection.execute("CREATE TABLE users(id int identity, name varchar(255), age int)")
#Start tranzakcji 1
# connection.execute("INSERT INTO users(name, age) VALUES ('Arek', 31), ('Jozef', 25)")
# #commit tranzakcji 1
# connection.commit()
# #Start trazakcji 2(nie utrwalono bo nie ma commita)
# connection.execute("INSERT INTO users(name, age) VALUES ('Artur', 15)")

cursor = connection.cursor()
cursor.execute("UPDATE users SET NAME='Nowe' WHERE name = 'Arek'")
cursor.commit()
print(f'{cursor.rowcount} wierszy zmienionych')
cursor.execute("SELECT NAME FROM users")
#print(cursor.fetchall())

cursor.close()
connection.close()
