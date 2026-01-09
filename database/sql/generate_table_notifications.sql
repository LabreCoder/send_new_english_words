CREATE TABLE notifications(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_id INTEGER NOT NULL,
    send_time TIMESTAMP NULL,
    FOREIGN KEY (word_id) REFERENCES words(id)
);