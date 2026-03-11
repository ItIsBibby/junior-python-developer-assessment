import sqlite3
from faker import Faker
import random

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

def populate_data():
    fake = Faker('en_GB')
    conn = sqlite3.connect('assessment.db')
    cursor = conn.cursor()

    for i in range(1, 51):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name.lower()}.{last_name.lower()}@example.com"
        status = random.choice(['active', 'suspended', 'archived'])
        
        cursor.execute(
            "INSERT INTO customers (id, first_name, surname, email, status) VALUES (?, ?, ?, ?, ?)",
            (i, first_name, last_name, email, status)
        )

        for _ in range(random.randint(1, 2)):
            product = random.choice(['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Desk Lamp'])
            qty = random.randint(1, 5)
            price = round(random.uniform(10.0, 500.0), 2)
            
            cursor.execute(
                "INSERT INTO orders (customer_id, product_name, quantity, unit_price) VALUES (?, ?, ?, ?)",
                (i, product, qty, price)
            )

    conn.commit()
    conn.close()
    print("50 customers and their orders have been generated.")

if __name__ == "__main__":
    initialise_database()
    populate_data()