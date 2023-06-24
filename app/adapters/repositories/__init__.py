import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Konfigurasi koneksi ke database PostgreSQL
DATABASE = os.environ.get('POSTGRES_DB')
USER = os.environ.get('POSTGRES_USER')
PASSWORD = os.environ.get('POSTGRES_PASSWORD')
HOST = os.environ.get('POSTGRES_HOST', 'localhost')
PORT = os.environ.get('POSTGRES_PORT', '5432')

# Membuat URL koneksi database
DB_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
# postgres+psycopg2

# Membuat engine SQLAlchemy
engine = create_engine(DB_URL)

# Membuat session factory
Session = sessionmaker(bind=engine)

# Membuat objek session
session = Session()