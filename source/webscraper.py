"""
Basic Web Scraper
------------------
This script scrapes data from a target website using BeautifulSoup and requests.

Technologies used:
- requests: for sending HTTP requests
- BeautifulSoup (bs4): for parsing HTML content
"""

import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        print(text)

