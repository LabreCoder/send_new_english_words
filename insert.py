import sqlite3

def insert_new_word(new_word, definition, example):
    conn, cursor = connect_sql()
    try:
        # Verificar se a palavra já existe
        cursor.execute("SELECT id FROM words WHERE word = ?", (new_word,))
        result = cursor.fetchone()
        
        if result:
            word_id = result[0]
        else:
            # Inserir nova palavra
            cursor.execute("INSERT INTO words (word) VALUES (?)", (new_word,))
            word_id = cursor.lastrowid
        
        # Inserir definição e notificação usando o mesmo cursor/conexão
        insert_definition(cursor, word_id, definition, example)
        insert_notifications(cursor, word_id)
        
        conn.commit()  # Commit apenas uma vez no final
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        disconnect_sql(conn)

def insert_definition(cursor, word_id, definition, example):
    cursor.execute("""
        INSERT INTO definitions (word_id, definition, example)
        VALUES (?, ?, ?)
    """, (word_id, definition, example))

def insert_notifications(cursor, word_id):
    cursor.execute("""
        INSERT INTO notifications (word_id, send_time)
        VALUES (?, CURRENT_TIMESTAMP)
    """, (word_id,))

def connect_sql():
    conn = sqlite3.connect('./database/data/database.db')
    cursor = conn.cursor()
    return conn, cursor

def disconnect_sql(conn):
    conn.close()