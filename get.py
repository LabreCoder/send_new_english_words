import sqlite3

def get_last_id():
    conn, cursor = connect_sql()
    try:
        cursor.execute("""
            SELECT id
            FROM words
            ORDER BY id DESC
            LIMIT 1
        """)
        row = cursor.fetchone()
        return row[0] if row else 0
    finally:
        disconnect_sql(conn)

def connect_sql():
    # Conectar ao banco
    conn = sqlite3.connect('./database/data/database.db')
    cursor = conn.cursor()
    
    return conn, cursor

def disconnect_sql(conn):
    conn.commit()
    conn.close()