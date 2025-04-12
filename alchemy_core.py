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
    echo=False
)

# query = sqlalchemy.text("SELECT * FROM workers WHERE pesel=:filter_pesel")
# result = connection.execute(query, {"filter_pesel": '1111111'})

metadata = sqlalchemy.MetaData()

worker_table = sqlalchemy.Table('workers', metadata,
                                sqlalchemy.Column('pesel', sqlalchemy.String(11), primary_key=True),
                                sqlalchemy.Column('first_name', sqlalchemy.String(255), nullable=False),
                                sqlalchemy.Column('last_name', sqlalchemy.String(255), nullable=False),
                                sqlalchemy.Column('birthday', sqlalchemy.Date),
                                sqlalchemy.Column('addresse_id', sqlalchemy.Integer)
                                )

connection = engine.connect()

query = sqlalchemy.select(worker_table)
result = connection.execute(query)
print(result.fetchall())
# # print(worker_table.columns.first_name)
# print('Andrzej' == 'Janek')
expression = worker_table.columns.first_name == 'Andrzej'
print(type(expression))
print(worker_table.columns.first_name == 'Andrzej')

query = sqlalchemy.select(
    worker_table.c.first_name,
    worker_table.c.last_name
)
result = connection.execute(query)
print(result.fetchall())

query = sqlalchemy.select(
    worker_table.c['first_name', 'last_name'])

result = connection.execute(query)
print(result.fetchall())

# Limit/top

query = sqlalchemy.select(worker_table).limit(2)
result = connection.execute(query)
print(result.fetchall())

# Sortowanie

query = sqlalchemy.select(worker_table) \
    .order_by(
    worker_table.c.first_name.desc(),

)
result = connection.execute(query)
print(result.fetchall())
# Filtrowanie

query = sqlalchemy.select(worker_table) \
    .where(worker_table.c.pesel == '1111111')
result = connection.execute(query)
print(result.fetchall())

# AND
query = sqlalchemy.select(worker_table) \
            .where((worker_table.c.addresse_id > 1) & (worker_table.c.addresse_id < 4))
result = connection.execute(query)
print(result.fetchall())

connection.close()
