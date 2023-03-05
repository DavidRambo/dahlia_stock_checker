"""main.py

Uses requests and BeautifulSoup4 to parse webstores selling select dahlias.
If they are in stock, send text message.
"""
import requests

from bs4 import BeautifulSoup as bs
