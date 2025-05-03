from werkzeug.security import check_password_hash, generate_password_hash
import db

# Retrieve a user by their ID
def get_user(user_id):
    sql = "SELECT id, username FROM users WHERE id = ?"
    results = db.query(sql, [user_id])
    return results[0] if results else None

# Retrieve all posts made by a specific user
def get_posts(user_id):
    sql = "SELECT id, title, image FROM posts WHERE user_id = ? ORDER BY id DESC"
    return db.query(sql, [user_id])

# Create a new user with a hashed password
def create_user(username, password):
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])

# Check user login credentials
def check_login(username, password):
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    results = db.query(sql, [username])
    if not results:
        return None

    user_id = results[0]["id"]
    password_hash = results[0]["password_hash"]
    if check_password_hash(password_hash, password):
        return user_id
    return None
