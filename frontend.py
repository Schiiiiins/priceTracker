import scraper
import db

db.create_table()

URL = input("Bitte Digitec-Link angeben: ")
desired_price = float(input("Wunschpreis angeben: "))

db.insert_data(scraper.check_price(URL, desired_price))
