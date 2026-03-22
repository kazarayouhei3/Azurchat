import sqlite3

import datetime
import json
from collections import defaultdict

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
    id TEXT NOT NULL,              -- ⭐ hipper
    username TEXT NOT NULL,        -- ⭐ userA
    friend_name TEXT NOT NULL,
    avatar TEXT,
    PRIMARY KEY (username, id)     -- ⭐ 关键！！
        )
    """)

    # ===== conversations（聊天列表）=====
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS conversations
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       username
                       TEXT
                       NOT
                       NULL,
                       friend_id
                       TEXT,
                       friend_name
                       TEXT
                       NOT
                       NULL,
                       avatar
                       TEXT,
                       last_message
                       TEXT,
                       last_time
                       DATETIME
                   )
                   """)
    # ⭐ 防止重复会话（非常关键）
    cursor.execute("""
    CREATE UNIQUE INDEX IF NOT EXISTS idx_user_friend
    ON conversations(username, friend_name)
    """)

    # ===== messages（聊天记录🔥）=====
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        conv_id INTEGER NOT NULL,
        sender TEXT NOT NULL,          -- user / ai
        content TEXT NOT NULL,
        time DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # ===== 索引优化（性能关键🔥）=====
    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_conv_id 
    ON messages(conv_id)
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_msg_time
    ON messages(time)
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_username
    ON conversations(username)
    """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS all_friends
                   (
                       id
                       TEXT
                       PRIMARY
                       KEY,
                       friend_name
                       TEXT,
                       faction
                       TEXT,
                       avatar
                       TEXT,
                       prompt
                       TEXT
                   )
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

def load_all_friends_from_json(json_path="prompt/info.json"):
    import os, json, sqlite3

    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, json_path)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    json_ids = set()

    for item in data:
        friend_id = item["id"]  # ⭐唯一id（hipper）
        json_ids.add(friend_id)

        cursor.execute("""
        INSERT INTO all_friends 
        (id, friend_name, faction, avatar, prompt)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
            friend_name=excluded.friend_name,
            faction=excluded.faction,
            avatar=excluded.avatar,
            prompt=excluded.prompt
        """, (
            friend_id,
            item["friend_name"],
            item.get("faction", ""),
            item.get("avatar", ""),
            item.get("prompt", "")
        ))

    # 删除多余数据
    cursor.execute("SELECT id FROM all_friends")
    db_ids = {row[0] for row in cursor.fetchall()}

    for id_ in db_ids - json_ids:
        cursor.execute("DELETE FROM all_friends WHERE id=?", (id_,))

    conn.commit()
    conn.close()
def get_groups_with_roles(db_path="chat.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT id, faction, friend_name, avatar
                   FROM all_friends
                   """)

    data = cursor.fetchall()
    conn.close()

    groups = defaultdict(list)

    for friend_id, faction, name, avatar in data:
        groups[faction].append({
            "id": friend_id,
            "name": name,
            "avatar": avatar
        })

    result = []

    for faction, items in groups.items():
        result.append({
            "name": faction,
            "items": items
        })

    return result
def get_friends_list(username):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT friend_name, avatar, id
    FROM friends
    WHERE username = ?
    """, (username,))

    data = cursor.fetchall()
    conn.close()

    result = []

    for name, avatar, fid in data:
        result.append({
            "id": fid,
            "name": name,
            "avatar": avatar
        })

    return result

def is_friend(username, friend_id):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 1 FROM friends
        WHERE username=? AND id=?
    """, (username, friend_id))

    result = cursor.fetchone()
    conn.close()

    return result is not None


def add_friend(username, friend_id, friend_name, avatar=None):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 1 FROM friends
        WHERE username=? AND id=?
    """, (username, friend_id))

    if cursor.fetchone():
        conn.close()
        return False

    cursor.execute("""
        INSERT INTO friends (id, username, friend_name, avatar)
        VALUES (?, ?, ?, ?)
    """, (friend_id, username, friend_name, avatar))

    conn.commit()
    conn.close()
    return True

def add_conversation(username, friend_id, friend_name, avatar=None):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 1 FROM conversations
        WHERE username=? AND friend_name=?
    """, (username, friend_name))

    if cursor.fetchone():
        conn.close()
        return False

    cursor.execute("""
        INSERT INTO conversations (
            username, friend_id, friend_name, avatar, last_message, last_time
        )
        VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    """, (username, friend_id, friend_name, avatar, ""))

    conn.commit()
    conn.close()
    return True

def get_conversations(username):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT friend_name, last_message, last_time, avatar
        FROM conversations
        WHERE username=?
        ORDER BY last_time DESC
    """, (username,))

    rows = cursor.fetchall()
    conn.close()
    return rows