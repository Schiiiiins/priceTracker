import sqlite3


def create_table():
    conn = sqlite3.connect("prices.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS pricelist (product text, actual_price real, desired_price real)")
    conn.commit()
    conn.close()


def insert_data(product, price_clean, des_price):
    conn = sqlite3.connect("prices.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO pricelist VALUES (?,?,?)", (product, price_clean, des_price))
    conn.commit()
    conn.close()


def view_data():
    conn = sqlite3.connect("prices.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows
