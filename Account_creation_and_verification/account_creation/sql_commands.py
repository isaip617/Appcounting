import sqlite3

def insert_username_and_password(username, password:str) -> None:
    """Insert a username and password into the 'accounts' table of the SQLite database."""

    connection = sqlite3.connect('Appcounting/account_sql_database/account_database.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO accounts (username, password) VALUES (?, ?);', 
    (username, password))
    
    connection.commit()
    connection.close()

def check_for_username(username:str) -> bool:
    """Checks how many times the username appears in the sql database, 
    if it is greater then 0 it will return true, and if is less than or
    equal to 0 it will return false."""

    connection = sqlite3.connect('Appcounting/account_sql_database/account_database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT COUNT(*) FROM accounts WHERE username = ?', (username,))
    count = cursor.fetchone()[0]

    connection.close()

    return count > 0