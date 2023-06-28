from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Alert, Price
from fastapi.encoders import jsonable_encoder
from sqlalchemy import desc


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

       

@router.get("/price")
async def get_price_history(data: Request, db: Session = Depends(get_db)):
    
    data = await data.json()
    coin_name = data["coin_name"]
    prices = db.query(Price).filter(Price.coin_name == coin_name).order_by(desc(Price.time)).all()
    prices_json = jsonable_encoder(prices)
    return {"prices": prices_json}


@router.post("/subscribe")
async def subscribe_alert(data: Request, db: Session = Depends(get_db)): 

    data = await data.json()
    email = data["email"]
    coin_name = data["coin_name"]
    diff = data["diff"]

    alert = Alert(email=email, coin_name=coin_name, diff=diff)  
  
    db.add(alert)
    db.commit()



@router.get("/alerts")
async def get_alerts(data: Request, db: Session = Depends(get_db)): 
    alerts = db.query(Alert).all()
    return {"alerts": alerts}

