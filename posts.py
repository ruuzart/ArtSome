import db

# Add a new post to the database
def add_post(title, descriptio, tags, user_id, image_data):
    sql = "INSERT INTO posts (title, descriptio, tags, user_id, image) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [title, descriptio, tags, user_id, image_data])

# Retrieve all posts from the database
def get_posts():
    sql = "SELECT id, title, descriptio, tags, image FROM posts ORDER BY id DESC"
    return db.query(sql)

# Retrieve a specific post by its ID
def get_post(post_id):
    sql = """
        SELECT posts.id, posts.title, posts.descriptio, posts.tags, posts.image, users.username, users.id user_id
        FROM posts
        JOIN users ON posts.user_id = users.id
        WHERE posts.id = ?
    """
    results = db.query(sql, [post_id])
    return results[0] if results else None

# Update a post's description and tags
def update_post(post_id, descriptio, tags):
    sql = "UPDATE posts SET descriptio = ?, tags = ? WHERE id = ?"
    db.execute(sql, [descriptio, tags, post_id])

# Remove a post from the database
def remove_post(post_id):
    sql = "DELETE FROM posts WHERE id = ?"
    db.execute(sql, [post_id])

# Find posts that match a query in their tags
def find_posts(query):
    sql = """SELECT id, title, descriptio, tags, image
            FROM posts
            WHERE tags LIKE ?
            ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like])

# Add a comment to a post
def add_comment(post_id, user_id, comment):
    sql = "INSERT INTO comments (post_id, user_id, comment) VALUES (?, ?, ?)"
    db.execute(sql, [post_id, user_id, comment])

# Retrieve comments for a post
def get_comments(post_id):
    sql = """
            SELECT comments.comment, users.id as user_id, users.username
            FROM comments
            LEFT JOIN users ON comments.user_id = users.id
            WHERE comments.post_id = ?
            ORDER BY comments.id DESC
            """
    return db.query(sql, [post_id])