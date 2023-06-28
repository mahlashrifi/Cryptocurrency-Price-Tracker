from sqlalchemy import create_engine, Column, ForeignKey, Integer, Float, String, Time
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///crypto.db", echo=True)

Base = declarative_base()

class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin_name = Column(String(50))
    time = Column(Time)
    price = Column(Float)

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50))
    coin_name = Column(String(50), ForeignKey("prices.coin_name"))
    diff = Column(Integer)

# Uncomment the following code to drop all database tables
# Base.metadata.drop_all(bind=engine)
# Create the database tables
Base.metadata.create_all(bind=engine)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)