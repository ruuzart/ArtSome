import db

def add_post(descriptio, user_id):
    sql = """INSERT INTO posts (descriptio, user_id)
            VALUES (?, ?)"""
    db.execute(sql, [descriptio, user_id])