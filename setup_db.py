import sqlite3

def create_database():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        country TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product TEXT,
        amount REAL,
        order_date TEXT,
        FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
    )''')

    customers = [
        (1, 'Ayush Rai', 'ayush@example.com', 'India'),
        (2, 'Jane Doe', 'jane@example.com', 'USA'),
        (3, 'Alex Smith', 'alex@example.com', 'UK')
    ]
    
    orders = [
        (101, 1, 'Laptop', 1200.50, '2026-05-01'),
        (102, 1, 'Mouse', 25.00, '2026-05-02'),
        (103, 2, 'Phone', 800.00, '2026-05-03'),
        (104, 3, 'Monitor', 300.00, '2026-05-04')
    ]

    cursor.executemany('INSERT OR IGNORE INTO customers VALUES (?,?,?,?)', customers)
    cursor.executemany('INSERT OR IGNORE INTO orders VALUES (?,?,?,?,?)', orders)

    conn.commit()
    conn.close()
    print("Database 'ecommerce.db' created successfully with sample data!")

if __name__ == "__main__":
    create_database()