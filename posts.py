import db

def add_post(descriptio, user_id):
    sql = """INSERT INTO posts (descriptio, user_id)
            VALUES (?, ?)"""
    db.execute(sql, [descriptio, user_id])

def get_posts():
    sql = "SELECT id, descriptio FROM posts ORDER BY id DESC"
    return db.query(sql)

def get_post(post_id):
    sql = """
        SELECT posts.descriptio, users.username
        FROM posts
        JOIN users ON posts.user_id = users.id
        WHERE posts.id = ?
    """
    results = db.query(sql, [post_id])
    return results[0] if results else None
