import db
from werkzeug.security import check_password_hash, generate_password_hash

def get_user(user_id):
    sql = "SELECT id, username FROM users WHERE id = ?"
    results = db.query(sql, [user_id])
    return results[0] if results else None

def get_posts(user_id):
    sql = "SELECT id, title, image FROM posts WHERE user_id = ? ORDER BY id DESC"
    return db.query(sql, [user_id])

def create_user(username, password):
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])

def check_login(username, password):
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    results = db.query(sql, [username])
    if not results:
        return None

    user_id = results[0]["id"]
    password_hash = results[0]["password_hash"]
    if check_password_hash(password_hash, password):
        return user_id
    else:
        return None