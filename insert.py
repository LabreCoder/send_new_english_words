import sqlite3

def insert_new_word(word, phrase):
    conn, cursor = connect_sql()
    try:
        cursor.execute("""
            INSERT INTO smtp_setting (word, phrase, send_time)
            VALUES (?, ?, date())
        """, (word, phrase))
        print(f'✅ Palavra "{word}" inserida com sucesso.')
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