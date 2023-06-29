from sqlalchemy import create_engine, Column, ForeignKey, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("mysql+pymysql://root:12345678@127.0.0.1:3306/crypto_tracker", echo=True)

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