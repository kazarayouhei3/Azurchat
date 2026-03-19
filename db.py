import sqlite3

import datetime

DB_PATH = "chat.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ===== users =====
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        api TEXT,
        url TEXT
    )
    """)

    # ===== friends（好友表）=====
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS friends (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,        -- 当前用户
        friend_name TEXT NOT NULL,    
        avatar TEXT                   
    )
    """)

    # ===== conversations（聊天列表）=====
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        friend_name TEXT NOT NULL,
        last_message TEXT,
        last_time TEXT
    )
    """)

    # ===== messages（聊天记录🔥）=====
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        conv_id INTEGER NOT NULL,
        sender TEXT NOT NULL,
        content TEXT NOT NULL,
        time TEXT
    )
    """)

    # ===== 索引（非常关键🔥）=====
    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_conv_id ON messages(conv_id)
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_username ON conversations(username)
    """)

    conn.commit()
    conn.close()

def get_conn():
    return sqlite3.connect(DB_PATH)

def check_user(username, password):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    )
    result = cursor.fetchone()

    conn.close()

    if result is None:
        return "not_exist"

    if result[0] == password:
        return "success"
    else:
        return "wrong_password"

def check_api(username):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT api, url FROM users WHERE username=?",
        (username,)
    )

    result = cursor.fetchone()
    conn.close()

    if result is None:
        return False

    api, url = result

    return bool(api and url)

def register_user(username, password):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM users WHERE username=?",
        (username,)
    )
    if cursor.fetchone():
        conn.close()
        return "exist"

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
    )

    conn.commit()
    conn.close()

    return "created"

def update_user_api(username, api, url):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET api=?, url=? WHERE username=?",
        (api, url, username)
    )

    conn.commit()
    conn.close()

def get_user_api(username):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT api, url FROM users WHERE username=?",
        (username,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0], result[1]
    return None, None

def get_conversations_with_avatar(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT c.friend_name, c.last_message, c.last_time, f.avatar
    FROM conversations c
    LEFT JOIN friends f
      ON c.friend_name = f.friend_name
     AND c.username = f.username
    WHERE c.username = ?
    ORDER BY c.last_time DESC
    """, (username,))

    data = cursor.fetchall()
    conn.close()
    return data

def get_conv_id(username, friend_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id FROM conversations
    WHERE username = ? AND friend_name = ?
    """, (username, friend_name))

    result = cursor.fetchone()
    conn.close()

    return result[0] if result else None

def insert_message(conv_id, sender, content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO messages (conv_id, sender, content, time)
    VALUES (?, ?, ?, ?)
    """, (conv_id, sender, content, now))

    conn.commit()
    conn.close()

def update_conversation(username, friend_name, msg):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    UPDATE conversations
    SET last_message = ?, last_time = ?, is_deleted = 0
    WHERE username = ? AND friend_name = ?
    """, (msg, now, username, friend_name))

    conn.commit()
    conn.close()
