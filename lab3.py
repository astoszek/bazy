import os
import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy import *
from sqlalchemy import create_engine

load_dotenv()

database_password = os.environ.get('DATABASE_PASSWORD')
suszi_login = 'stoszek'
server = 'morfeusz.wszib.edu.pl'
driver = 'ODBC+Driver+17+for+SQL+Server'

# dialect+driver://username:password@host:port/database?dodtkowe_opcje_klucz_wartość
engine = create_engine(
    f'mssql+pyodbc://{suszi_login}:{database_password}@{server}/{suszi_login}?driver={driver}&Encrypt=no',
    echo=False
)

metadata = MetaData()

worker_table = Table('workers', metadata,
                     Column('pesel', String(11), primary_key=True),
                     Column('first_name', String(255), nullable=False),
                     Column('last_name', String(255), nullable=False),
                     Column('birthday', Date, nullable=False),
                     Column('address_id', Integer, ForeignKey('address.address_id'))
                     )

address_table = Table('address', metadata,
                      Column('address_id', Integer, primary_key=True, autoincrement=True),
                      Column('country', String(255), nullable=False),
                      Column('city', String(255), nullable=False),
                      Column('street', String(255), nullable=False),
                      Column('postal_code', String(255), nullable=False)
                      )

connection = engine.connect()

if __name__ == '__main__':
    # a. Wszystkie adresy znajdujące się w Warszawie. Pobierz kolumny: Kraj, Miasto

    query = sqlalchemy.select(address_table.c.country, address_table.c.city).where(address_table.c.city == "Warszawa")
    result = connection.execute(query)
    print(result.fetchall())

# b. Wszyscy pracownicy posortowani po dacie urodzenia w sposób malejący

query = sqlalchemy.select(worker_table).order_by(worker_table.c.birthday.desc())
result = connection.execute(query)
print(result.fetchall())
# c. Wszyscy pracownicy, których imię zaczyna się na literę A lub M. Pobierz tylko kolumny: Imię, Nazwisko


query_ = sqlalchemy.select(worker_table.c.first_name, worker_table.c.last_name).where(
    or_(
        worker_table.c.first_name.like("A%"),
        worker_table.c.first_name.like("M%")
    )
)
result = connection.execute(query)
print(result.fetchall())
# d. Wszyscy pracownicy, którzy mieszkają w Warszawie

query = sqlalchemy.select(worker_table).join(address_table, worker_table.c.address_id == address_table.c.address_id) \
    .where(address_table.c.city == "Warszawa")

result = connection.execute(query)
print(result.fetchall())
# e. Liczba pracowników mieszkających w danym mieście

query = sqlalchemy.select(address_table.c.city, func.count(worker_table.c.pesel).label("worker_count")) \
    .join(address_table, worker_table.c.address_id == address_table.c.address_id).group_by(address_table.c.city)

result = connection.execute(query)
print(result.fetchall())
