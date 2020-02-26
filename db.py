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
    cur.execute("SELECT * FROM pricelist")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_data(item):
    conn = sqlite3.connect("prices.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM pricelist WHERE item=?", (item,))
    conn.commit()
    conn.close()


def update_desprice(des_price, item):
    conn = sqlite3.connect("prices.db")
    cur = conn.cursor()
    cur.execute("UPDATE pricelist SET desired_price=? WHERE item=?", (des_price, item))
    conn.commit()
    conn.close()
