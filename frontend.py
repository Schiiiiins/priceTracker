import scraper

URL = input("Bitte Digitec-Link angeben: ")
desired_price = float(input("Wunschpreis angeben: "))

scraper.check_price(URL, desired_price)
