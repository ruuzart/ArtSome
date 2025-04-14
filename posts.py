import db

def add_post(title, descriptio, tags, user_id):
    sql = "INSERT INTO posts (title, descriptio, tags, user_id) VALUES (?, ?, ?, ?)"
    db.execute(sql, [title, descriptio, tags, user_id])

def get_posts():
    sql = "SELECT id, title, descriptio, tags FROM posts ORDER BY id DESC"
    return db.query(sql)

def get_post(post_id):
    sql = """
        SELECT posts.id, posts.title, posts.descriptio, posts.tags, users.username, users.id user_id
        FROM posts
        JOIN users ON posts.user_id = users.id
        WHERE posts.id = ?
    """
    results = db.query(sql, [post_id])
    return results[0] if results else None

def update_post(post_id, descriptio, tags):
    sql = "UPDATE posts SET descriptio = ?, tags = ? WHERE id = ?"
    db.execute(sql, [descriptio, tags, post_id])

def remove_post(post_id):
    sql = "DELETE FROM posts WHERE id = ?"
    db.execute(sql, [post_id])

def find_posts(query):
    sql = """SELECT id, title, descriptio, tags
            FROM posts
            WHERE title LIKE ? OR descriptio LIKE ? OR tags LIKE ?
            ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like, like])