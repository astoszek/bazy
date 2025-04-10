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
if __name__ == '__main__':
    #connection.execute("CREATE TABLE users(id int identity, name varchar(255), age int)")
    #Start tranzakcji 1
    # connection.execute("INSERT INTO users(name, age) VALUES ('Arek', 31), ('Jozef', 25)")
    # #commit tranzakcji 1
    # connection.commit()
    # #Start trazakcji 2(nie utrwalono bo nie ma commita)
    # connection.execute("INSERT INTO users(name, age) VALUES ('Artur', 15)")

        cursor = connection.cursor()
        new_name = input('Podaj nowe imię: ')
        old_name = input('Podaj stare imię: ')
        #cursor.execute(f"UPDATE users SET NAME='{new_name}' WHERE name = 'Nowe'")
        cursor.execute(f"UPDATE users SET NAME=? WHERE name = ?", (new_name, old_name))
        cursor.commit()
        print(f'{cursor.rowcount} wierszy zmienionych')
        cursor.execute("SELECT NAME FROM users")

        #print(cursor.fetchall())

        cursor.close()
        connection.close()
