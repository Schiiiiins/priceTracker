import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}


def send_mail():
    pass


def check_price(URL, desired_price):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_="productName").get_text()
    price = soup.select_one('div[class="ZZ8f"] strong').get_text(strip=True)

    if("–" in price):
        price_clean = price.replace("–", "00")
    else:
        price_clean = price

    print(title)
    print(price_clean)
    
    #if price_striped < desired_price:
        #send_mail()
