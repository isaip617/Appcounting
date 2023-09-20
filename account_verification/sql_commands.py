import sqlite3

db_file = 'account_sql_database/account_database.db'

def check_for_username(username:str) -> bool:
    """
    Checks how many times the username appears in the sql database, 
    if it is greater then 0 it will return true, and if is less than or
    equal to 0 it will return false.
    """

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute('SELECT COUNT(*) FROM accounts WHERE username = ?', (username,))
    count = cursor.fetchone()[0]

    connection.close()

    return count == 1

def check_password(username, password:str) -> bool:
    """
    This function connects to a SQLite database, retrieves the stored password associated with the provided username,
    and compares it with the provided password. If the stored password exists and matches the provided password,
    the function returns True; otherwise, it returns False.
    """

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    database_password = cursor.fetchone()[0]
    connection.close()
    
    if database_password:
        return password == database_password
    else:
        return False
