import sqlite3

conn = sqlite3.connect("feedback.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS feedback (code TEXT, suggestion TEXT, accepted BOOLEAN)")
conn.commit()

def save_feedback(code, suggestion, accepted):
    cursor.execute("INSERT INTO feedback VALUES (?, ?, ?)", (code, suggestion, accepted))
    conn.commit()
