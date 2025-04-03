import os
from dotenv import load_dotenv

load_dotenv()
database_password = os.environ.get('DATABASE_PASSWORD')
suszi_login = "stoszek"
server = "morfeusz.wszib.edu.pl"