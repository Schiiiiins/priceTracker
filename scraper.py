import requests
from bs4 import BeautifulSoup
import db

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

db.create_table()

def send_mail():
    pass


def check_price(URL, desired_price):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_name = soup.find(class_="productName").get_text()
    price = soup.select_one('div[class="Z19v"] strong').get_text(strip=True)

    if("–" in price):
        price_clean = float(price.replace("–", "00"))
    else:
        price_clean = float(price)
	
    db.insert_data(product_name, price_clean, desired_price)
    
