from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Alert, Price, Coin
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
    
    coin_name = data.query_params.get("q")
    coin = db.query(Coin).filter(Coin.name == coin_name).first()
    if coin is None:
        coin = Coin(name=coin_name)
        db.add(coin)
        db.commit()
    prices = db.query(Price).filter(Price.coin == coin.id).order_by(desc(Price.time)).all()
    return jsonable_encoder({
      'coin_name': coin_name,
      'prices': prices       
    })


@router.post("/subscribe")
async def subscribe_alert(data: Request, db: Session = Depends(get_db)): 

    data = await data.json()
    email = data["email"]
    coin_name = data["coin_name"]
    diff = data["diff"]

    coin = db.query(Coin).filter(Coin.name == coin_name).first()
    if coin is None:
        coin = Coin(name=coin_name)
        db.add(coin)
        db.commit()

    alert = Alert(email=email, coin=coin.id, diff=diff)  
  
    db.add(alert)
    db.commit()



@router.get("/alerts")
async def get_alerts(data: Request, db: Session = Depends(get_db)): 
    alerts = db.query(Alert).all()
    return {"alerts": alerts}


