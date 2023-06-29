#Add some hardcode prices to prices_table 
from datetime import datetime
from sqlalchemy.orm import Session
from database import SessionLocal, Price, Alert

def add_price_to_database(db: Session):

    prices = [
        Price(coin_name="BTC", datetime=datetime(2023, 6, 1, 9, 30), price=50000.0),
        Price(coin_name="BTC", datetime=datetime(2021, 6, 1, 10, 0), price=3000.0),
        Price(coin_name="LTC", datetime=datetime(2023, 6, 1, 11, 15), price=150.0),
        Price(coin_name="LTC", datetime=datetime(2021, 6, 1, 11, 15), price=2.0),
        Price(coin_name="ETH", datetime=datetime(2023, 6, 1, 11, 15), price=150.0),
    ]
    db.add_all(prices)
    db.commit()

def add_alerts_to_database(db: Session):    

    alerts = [
        Alert(email="mahla7997@gmail.com", coin_name="BTC", diff=5),
        Alert(email="mahla7997@gmail.com", coin_name="BTC", diff=10),
        Alert(email="mahla7997@gmail.com", coin_name="BTC", diff=20),
        Alert(email="mahla7997@gmail.com", coin_name="BTC", diff=90),
        Alert(email="mahla7997@gmail.com", coin_name="ETH", diff=5),
        Alert(email="mahla7997@gmail.com", coin_name="ETH", diff=15),
        Alert(email="mahla7997@gmail.com", coin_name="ETH", diff=30),
        Alert(email="mahla7997@gmail.com", coin_name="LTC", diff=5),
        Alert(email="mahla7997@gmail.com", coin_name="LTC", diff=20),
    ]

    db.add_all(alerts)
    db.commit()


db = SessionLocal()
try :
    add_price_to_database(db)
    add_alerts_to_database(db)
finally :
        db.close()



