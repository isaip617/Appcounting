import sqlite3

conn = sqlite3.connect('account_database.db')


conn.execute('PRAGMA foreign_keys = ON')

cursor = conn.cursor()

sql_statements = [
    '''CREATE TABLE accounts (
        username TEXT NOT NULL PRIMARY KEY,
        password TEXT NOT NULL
    )''',

    '''CREATE TABLE food_spending (
        username TEXT NOT NULL,
        date TEXT NOT NULL,
        food_item TEXT NOT NULL,
        food_price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (username) REFERENCES accounts(username)
    )''',

    '''CREATE TABLE clothes_spending (
        username TEXT NOT NULL,
        date TEXT NOT NULL,
        clothes_item TEXT NOT NULL,
        clothes_item_price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (username) REFERENCES accounts(username)
    )''',

    '''CREATE TABLE housing_spending (
        username TEXT NOT NULL,
        date TEXT NOT NULL,
        housing_item TEXT NOT NULL,
        housing_item_price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (username) REFERENCES accounts(username)
    )''',

    '''CREATE TABLE utilities_spending (
        username TEXT NOT NULL,
        date TEXT NOT NULL,
        utilities_item TEXT NOT NULL,
        utilities_item_price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (username) REFERENCES accounts(username)
    )''',

    '''CREATE TABLE transportation_spending (
        username TEXT NOT NULL,
        date TEXT NOT NULL,
        transportation_item TEXT NOT NULL,
        transportation_item_price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (username) REFERENCES accounts(username)
    )''',

    '''CREATE TABLE personal_spending (
        username TEXT NOT NULL,
        date TEXT NOT NULL,
        personal_item TEXT NOT NULL,
        personal_item_price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (username) REFERENCES accounts(username)
    )''',

    '''CREATE TABLE medical_spending (
        username TEXT NOT NULL,
        date TEXT NOT NULL,
        medical_item TEXT NOT NULL,
        medical_item_price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (username) REFERENCES accounts(username)
    )''',

    '''CREATE TABLE savings_account_categories (
        username TEXT NOT NULL,
        retirement_fund DECIMAL(10, 2) NOT NULL,
        emergency_fund DECIMAL(10, 2) NOT NULL,
        childrens_college_fund DECIMAL(10, 2) NOT NULL,
        big_purchase_savings_1 DECIMAL(10, 2) NOT NULL,
        big_purchase_savings_2 DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (username) REFERENCES accounts(username)
    )'''
]

for statement in sql_statements:
    cursor.execute(statement)
conn.commit()
conn.close()
