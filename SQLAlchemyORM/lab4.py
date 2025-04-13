import os
import datetime
from sqlalchemy import *
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from alchemy_orm import Base

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

Session = sessionmaker(engine)

if __name__ == '__main__':
    # session = Session()
    # session.execute(CreateSchema('library_orm'))
    # session.commit()

    Base.metadata.create_all(engine)

cart_product = Table(
    'cart_product',
    Base.metadata,
    Column('cart_id', Integer, ForeignKey('carts.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True)
)


# 1. Użytkownik
class User(Base):
    __tablename__ = 'users'

    id : Column(Integer, primary_key=True)
    first_name: Column(String, nullable=False)
    last_name: Column(String, nullable=False)

    shipping_address = relationship("ShippingAddress", uselist=False, back_populates="user")

    carts = relationship("Cart", back_populates="user")


# 2. Adres dostawy
class ShippingAddress(Base):
    __tablename__ = 'shipping_addresses'

    id: Column(Integer, primary_key=True)
    country: Column(String, nullable=False)
    city: Column(String, nullable=False)
    postal_code: Column(String, nullable=False)
    building_number: Column(String, nullable=False)
    apartment_number: Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False)

    user = relationship("User", back_populates="shipping_address")


# 3. Koszyk
class Cart(Base):
    __tablename__ = 'carts'

    id: Column(Integer, primary_key=True)
    created_at: Column(DateTime, default=datetime.utcnow)

    user_id: Column(Integer, ForeignKey('users.id'), nullable=False)
    user: relationship("User", back_populates="carts")

    products = relationship("Product", secondary=cart_product, back_populates="carts")


# 4. Produkt
class Product(Base):
    __tablename__ = 'products'

    id: Column(Integer, primary_key=True)
    title: Column(String, nullable=False)
    description: Column(String, nullable=False)
    price: Column(Float, nullable=False)

    carts = relationship("Cart", secondary=cart_product, back_populates="products")
