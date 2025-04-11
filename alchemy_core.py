import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import sqlalchemy

load_dotenv()

database_password = os.environ.get('DATABASE_PASSWORD')
suszi_login = 'stoszek'
server = 'morfeusz.wszib.edu.pl'
driver = 'ODBC+Driver+17+for+SQL+Server'

# dialect+driver://username:password@host:port/database?dodatkowe_opcje_klucz_wartość
engine = create_engine(
    f'mssql+pyodbc://{suszi_login}:{database_password}@{server}/{suszi_login}?driver={driver}&Encrypt=no',
    echo=True
)

# query = sqlalchemy.text("SELECT * FROM workers WHERE pesel=:filter_pesel")
# result = connection.execute(query, {"filter_pesel": '1111111'})

metadata = sqlalchemy.MetaData()

worker_table = sqlalchemy.Table('workers', metadata,
                                sqlalchemy.Column('pesel', sqlalchemy.String(11), primary_key=True),
                                sqlalchemy.Column('first_name', sqlalchemy.String(255), nullable=False),
                                sqlalchemy.Column('last_name', sqlalchemy.String(255), nullable=False),
                                sqlalchemy.Column('birthday', sqlalchemy.Date)
                                )

connection = engine.connect()

query = sqlalchemy.select(worker_table)
result = connection.execute(query)
print(result.fetchall())

connection.close()
