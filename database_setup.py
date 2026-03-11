import sqlite3
from faker import Faker

def initialise_database():
    conn = sqlite3.connect('assessment.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS orders")
    cursor.execute("DROP TABLE IF EXISTS customers")

    cursor.execute('''
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            surname TEXT,
            email TEXT,
            status TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            product_name TEXT,
            quantity INTEGER,
            unit_price REAL,
            FOREIGN KEY (customer_id) REFERENCES customers (id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database initialised successfully.")

if __name__ == "__main__":
    initialise_database()
