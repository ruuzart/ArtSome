import sqlite3
from flask import g

# Establish a connection to the SQLite database
def get_connection():
    con = sqlite3.connect("database.db")
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con

# Execute a SQL command and commit changes to the database
def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()

# Retrieve the last inserted row ID from the database
def last_insert_id():
    return g.last_insert_id 

# Execute a SQL query and return the results
def query(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params).fetchall()
    con.close()
    return result
