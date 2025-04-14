import db

def get_user(user_id):
    sql = "SELECT id, username FROM users WHERE id = ?"
    results = db.query(sql, [user_id])
    return results[0] if results else None

def get_posts(user_id):
    sql = "SELECT id, title FROM posts WHERE user_id = ? ORDER BY id DESC"
    return db.query(sql, [user_id])