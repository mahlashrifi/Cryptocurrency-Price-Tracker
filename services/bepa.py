import configparser
import requests 
from sqlalchemy.orm import Session
from database import SessionLocal, Alert, Price
from sqlalchemy import desc
from datetime import datetime

def get_db():
    db = SessionLocal()
    return db



config = configparser.ConfigParser()
config.read('config.ini')


def get_data(db: Session):
    port = config.get('Coinnews', 'PORT')
    response = requests.get(f"https://localhost:{port}/api/data")
    currency_list = list(response.json)

    # Send request to get coin price
    for coin in currency_list :
        response = requests.get(f"https://localhost:{port}/api/data/{coin}")
        price = response.json["value"]
        datetime = datetime.fromisoformat(response.json["updated_at"]) 

        price_obj = Price(coin_name=coin, datetime=datetime, price=price )
        db.add(price_obj)
        db.commit()



def handle_subscription(db: Session):
    # Get all available currencies

    port = config.get('Coinnews', 'PORT')
    
    # Get the available currencies from the API
    
    response = requests.get(f"https://localhost:{port}/api/data")
    currency_list = list(response.json)
    
   
    
    # handle alarming process for each available coin
    for coin in currency_list:
        # Get the changes for the current coin from Coinnews API
        response = requests.get(f"https://localhost:{port}/api/data/{coin['name']}/history")
        price_changes = list(response.json())
       
        # Last price of coin in table
        last_price = db.query(Price).filter(Price.coin_name == coin["name"]).order_by(desc(Price.datetime)).first()

        if last_price is not None:
            last_price_date = last_price.datetime
            #Get the total amount of changes that have occurred since the last price was recorded
            total_change = 0
            for change in price_changes:
                change_time = datetime.fromisoformat(change["date"])
                if (change_time > last_price_date):
                    total_change+= change['value']

            # Find percentage of coin price changes
            percentage_diff = (total_change - last_price.price) / last_price.price
            
            #The list of all subscriptions to be notified according to the percentage of difference obtained
            coin_subs = db.query(Alert).filter(Alert.coin_name == coin["name"]).all()
            target_subs = []   
            for subscription in coin_subs:
                if abs(percentage_diff) >= subscription.diff:
                    target_subs.append(subscription)
       

            #Notify each target subscriptions by email 
            for subscription in target_subs :
                handle_email_sending(subscription, percentage_diff)
        

#This method handle subject, messages and information needed to be send an email 
def handle_email_sending(subscription, percentage_diff):
    subject = f"Notice regarding {subscription.coin_name} price changes"
    email = subscription.email
    text = f"Bitcoin price change = {percentage_diff}%"
    
    send_email(subject, email, text)


def send_email(subject, email, text):
    domin_name = config.get('Mailgun', 'DOMIN_NAME')
    api_key = config.get('Mailgun', 'API_KEY')
    print(f"subject={subject} email={email} text={text}")
    response = requests.post(
        "https://api.mailgun.net/v3/"+domin_name+"/messages",
        auth=("api", api_key),
        data={"from": "CryptoCurrencyTracker@service.com",
              "to": f"<{email}>",
              "subject": f"<{subject}>",
              "text": f"<{text}>"})

   

db = SessionLocal()
try :
    handle_subscription(db)
finally :   
    db.close()