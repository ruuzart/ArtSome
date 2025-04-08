import db

def add_post(title, descriptio, user_id):
    sql = "INSERT INTO posts (title, descriptio, user_id) VALUES (?, ?, ?)"
    db.execute(sql, [title, descriptio, user_id])

def get_posts():
    sql = "SELECT id, title, descriptio FROM posts ORDER BY id DESC"
    return db.query(sql)

def get_post(post_id):
    sql = """
        SELECT posts.id, posts.title, posts.descriptio, users.username, users.id user_id
        FROM posts
        JOIN users ON posts.user_id = users.id
        WHERE posts.id = ?
    """
    results = db.query(sql, [post_id])
    return results[0] if results else None


def update_post_descriptio(post_id, descriptio):
    sql = "UPDATE posts SET descriptio = ? WHERE id = ?"
    db.execute(sql, [descriptio, post_id])