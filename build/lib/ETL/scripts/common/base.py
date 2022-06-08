from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
import psycopg2

# ruth of the SQL
# postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]

ruth = 'postgresql+psycopg2://postgres:sam31415@localhost:5432/postgres'

# Create an engine
engine = create_engine(ruth,echo=True)

# Connection
conn = engine.connect()

# Create a session
session = Session(engine)

# Initialize the declarative base
Base = declarative_base()
