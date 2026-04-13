# Using a common library like psycopg2 or sqlite3
import sqlite3

def get_user(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Use parameterized queries (placeholders)
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,)) # The library handles escaping
    
    return cursor.fetchone()
