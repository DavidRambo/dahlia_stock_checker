"""main.py

Uses requests and BeautifulSoup4 to parse webstores selling select dahlias.
If they are in stock, send text message using twilio.
I have a separate scripts directory that has a copy of this script with my
twilio account information.
"""
from bs4 import BeautifulSoup as bs
import requests


url = "https://www.creeksidedahlias.com/store/p534/KA%27S_Khaleesi.html"
response = requests.get(url)

print("Status code: ", response)

soup = bs(response.text, "html.parser")

"""The out of stock message string is
'\n\t\t\t\t\t\t\tSold out\n\t\t\t\t\t\t'
"""
oos_msg = "\n\t\t\t\t\t\t\tSold out\n\t\t\t\t\t\t"
oos_tag = soup.find(id="wsite-com-product-inventory-out-of-stock-message")

if oos_tag and oos_tag.string == oos_msg:
    pass
else:
    # Probably in stock, send alert.
    print("In Stock!")
