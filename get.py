import sqlite3

def get_last_id():
    conn, cursor = connect_sql()
    try:
        cursor.execute("""
            SELECT COUNT(*)
            FROM words
            ORDER BY id DESC
            LIMIT 1
        """)
        row = cursor.fetchone()
        return row[0] if row else 0
    finally:
        disconnect_sql(conn)

def check_word(word):
    conn, cursos = connect_sql()
    try:
        cursos.execute("""
            SELECT word
            FROM words
            WHERE word = ?
        """, (word,))
        row = cursos.fetchone()
        return True if row else False
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