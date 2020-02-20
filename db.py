import sqlite3


def create_table():
    conn = sqlite3.connect("prices.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (product TEXT, price REAL)")
    conn.commit()
    conn.close()


def insert_data(product_name, price_clean):
    conn = sqlite3.connect("prices.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?)", (product_name, price_clean))
    conn.commit()
    conn.close()


def view_data():
    conn = sqlite3.connect("prices.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows
