from sqlalchemy import create_engine, Column, ForeignKey, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import os

DATABASE = {
    'name': 'crypto_tracker',
    'user': os.getenv("POSTGRES_USER"),
    'password': os.getenv("POSTGRES_PASSWORD"),
    'host': os.getenv("POSTGRES_HOST"),
    'port': 5432,
}

# Create an engine instance
engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{name}'.format(**DATABASE))

Base = declarative_base()

class Coin(Base):
    __tablename__ = "coins"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(Integer, ForeignKey("coins.id"))
    time = Column(DateTime)
    price = Column(Float)

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50))
    coin = Column(Integer, ForeignKey("coins.id"))
    diff = Column(Integer)

# Uncomment the following code to drop all database tables
# Base.metadata.drop_all(bind=engine)
# Create the database tables
Base.metadata.create_all(bind=engine)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)