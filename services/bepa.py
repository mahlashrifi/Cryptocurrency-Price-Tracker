
import configparser
import requests 


config = configparser.ConfigParser()
config.read('config.ini')
domin_name = config.get('Mailgun', 'DOMIN_NAME')
api_key = config.get('Mailgun', 'API_KEY')


def send_email(subject, email, text):
    response = requests.post(
        "https://api.mailgun.net/v3/"+domin_name+"/messages",
        auth=("api", api_key),
        data={"from": "CryptoCurrencyTracker@service.com",
              "to": f"<{email}>",
              "subject": f"<{subject}>",
              "text": f"<{text}>"})

