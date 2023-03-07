"""main.py

Uses requests and BeautifulSoup4 to parse webstores selling select dahlias.
If they are in stock, send text message using twilio.
I have a separate scripts directory that has a copy of this script with my
twilio account information.
"""
import logging
import os

from bs4 import BeautifulSoup as bs
import requests
from twilio.rest import Client


# Setup logging file so that there is a record of in-stock results.
logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%m/%d%Y %I:%M:%S %p",
    filename="dahlia.log",
    encoding="utf-8",
    level=logging.INFO,
)

# Setup Twilio environment variables
account_sid = "placeholder"
auth_token = os.environ["TWILIO_AUTH_TOKEN"]


url = "https://www.creeksidedahlias.com/store/p534/KA%27S_Khaleesi.html"
response = requests.get(url)

# print("Status code: ", response)

soup = bs(response.text, "html.parser")

"""The out of stock message string is
'\n\t\t\t\t\t\t\tSold out\n\t\t\t\t\t\t'
"""
oos_msg = "\n\t\t\t\t\t\t\tSold out\n\t\t\t\t\t\t"
oos_tag = soup.find(id="wsite-com-product-inventory-out-of-stock-message")

if oos_tag and oos_tag.string == oos_msg:
    print("Out of stock :(")
else:
    # Probably in stock, send alert.
    # But only if an alert was not already sent.
    with open("dahlia.log", "r") as f:
        log_text = f.read()
    if log_text:
        logging.info("In stock.")
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="KA Dahlia is in stock at Creekside Dahlias.",
            from_="your virtual phone number",
            to="your destination phone number",
        )
