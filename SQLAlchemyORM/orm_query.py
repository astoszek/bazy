from orm_connection import Session
from sqlalchemy import *
from alchemy_orm import Author

session = Session()

select_authors = select(Author)
all_authors = session.execute(select_authors).all()
print(all_authors)