import base64
import secrets
import sqlite3

from flask import Flask, abort, flash, redirect, render_template, request, session

import config
import posts
import users

app = Flask(__name__)
app.secret_key = config.secret_key

# Ensure the user is logged in; abort if not
def require_login():
    if "user_id" not in session:
        abort(403)

# Validate CSRF token; abort if invalid
def check_csrf():
    if "csrf_token" not in request.form:
        abort(403)
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

# Route for the main page, displaying all posts
@app.route("/")
def index():
    all_posts = posts.get_posts()
    return render_template("index.html", posts=all_posts)

# Template filter to convert data to base64 encoding
@app.template_filter("to_base64")
def to_base64(data):
    if data is None:
        return ""
    return base64.b64encode(data).decode("utf-8")

# Route to display a specific user's profile and their posts
@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    user_posts = users.get_posts(user_id)
    return render_template("show_user.html", user=user, posts=user_posts)

# Route to search for posts based on a query
@app.route("/find_post", methods=["GET"])
def find_post():
    query = request.args.get("query")
    if query:
        results = posts.find_posts(query)
    else:
        query = ""
        results = []
    return render_template("find_post.html", query=query, results=results)

# Route to display a specific post and its comments
@app.route("/post/<int:post_id>")
def show_post(post_id):
    post = posts.get_post(post_id)
    if not post:
        abort(404)
    comments = posts.get_comments(post_id)
    return render_template("show_post.html", post=post, comments=comments)

# Route to show the form for creating a new post
@app.route("/new_post")
def new_post():
    require_login()
    return render_template("new_post.html")

# Route to handle the creation of a new post
@app.route("/create_post", methods=["POST"])
def create_post():
    require_login()
    check_csrf()
    title = request.form["title"]
    if not title or len(title) > 100:
        abort(403)
    descriptio = request.form["descriptio"]
    if len(descriptio) > 1000:
        abort(403)
    tags = request.form["tags"]
    user_id = session["user_id"]

    if "image" not in request.files:
        abort(403)
    image = request.files["image"]
    if image.filename == "":
        abort(403)
    if not (image.filename.endswith(".jpg") or image.filename.endswith(".png")):
        flash("ERROR: wrong file format")
        return redirect("/new_post")
    image_data = image.read()

    posts.add_post(title, descriptio, tags, user_id, image_data)
    return redirect("/")

# Route to handle adding a comment to a post
@app.route("/post/create_comment", methods=["POST"])
def create_comment():
    require_login()
    check_csrf()
    post_id = int(request.form["post_id"])
    post = posts.get_post(post_id)
    if not post:
        abort(403)
    comment = request.form["comment"]
    if len(comment) > 200:
        abort(403)
    user_id = int(session["user_id"])

    posts.add_comment(post_id, user_id, comment)
    return redirect(f"/post/{post_id}")

# Route to show the form for editing a post
@app.route("/edit_post/<int:post_id>")
def edit_post(post_id):
    require_login()
    post = posts.get_post(post_id)
    if not post:
        abort(404)
    if post["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_post.html", post=post)

# Route to handle updating a post
@app.route("/update_post/<int:post_id>", methods=["POST"])
def update_post(post_id):
    require_login()
    check_csrf()
    post = posts.get_post(post_id)
    if not post:
        abort(404)
    if post["user_id"] != session["user_id"]:
        abort(403)

    descriptio = request.form["descriptio"]
    if len(descriptio) > 1000:
        abort(403)
    tags = request.form["tags"]

    posts.update_post(post_id, descriptio, tags)
    return redirect(f"/post/{post_id}")

# Route to handle removing a post
@app.route("/remove_post/<int:post_id>", methods=["GET", "POST"])
def remove_post(post_id):
    require_login()
    post = posts.get_post(post_id)
    if not post:
        abort(404)
    if post["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_post.html", post=post)
    if request.method == "POST":
        check_csrf()
        if "remove" in request.form:
            posts.remove_post(post_id)
            return redirect("/")
        return redirect(f"/post/{post_id}")

# Route to display the registration form
@app.route("/register")
def register():
    return render_template("register.html")

# Route to handle user registration
@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    if username == "":
        abort(403)
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 == "":
        abort(403)
    if password1 != password2:
        return "ERROR: passwords do not match"
    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        return "ERROR: username taken"
    return redirect("/login")

# Route to handle user login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        if username == "":
            abort(403)
        password = request.form["password"]
        if password == "":
            abort(403)

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        return "ERROR: wrong username or password"

# Route to handle user logout
@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")