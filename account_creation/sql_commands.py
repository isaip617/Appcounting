import sqlite3

def insert_username_and_password(username, password:str) -> None:
    """Insert a username and password into the 'accounts' table of the SQLite database."""

    connection = sqlite3.connect('/Users/isaip617/Desktop/Appcounting/account_sql_database/account_database.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO accounts (username, password) VALUES (?, ?);', 
    (username, password))
    connection.commit()
    connection.close()