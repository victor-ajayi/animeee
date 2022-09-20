import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session.__init__ import Session
from helpers import login_required, lookup
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure database with CS50
db = SQL("sqlite:///data.db")


@app.errorhandler(404)
def invalid_route(e):
    return "This page does not exist."


@app.route("/add_favourite", methods=["POST"])
@login_required
def add_favourite():

    title = request.form.get("title")
    db.execute("INSERT INTO favourites (id, title) VALUES (?, ?)",
               session["user_id"], title)

    return redirect("/favourites")


@app.route("/add_watched", methods=["POST"])
@login_required
def add_watched():

    title = request.form.get("title")
    db.execute("INSERT INTO watched (id, title) VALUES (?, ?)",
               session["user_id"], title)

    return redirect("/watched")


@app.route("/add_watching", methods=["POST"])
@login_required
def add_watching():

    title = request.form.get("title")
    db.execute("INSERT INTO watching (id, title) VALUES (?, ?)",
               session["user_id"], title)

    return redirect("/watching")


@app.route("/delete")
@login_required
def delete():

    if request.args.get("delete") == "watched":
        db.execute("DELETE FROM watched WHERE id = ? AND title = ?",
                   session["user_id"], request.args.get("title"))
        return redirect("/watched")

    elif request.args.get("delete") == "favourites":
        db.execute("DELETE FROM favourites WHERE id = ? AND title = ?",
                   session["user_id"], request.args.get("title"))
        return redirect("/favourites")

    else:
        db.execute("DELETE FROM watching WHERE id = ? AND title = ?",
                   session["user_id"], request.args.get("title"))
        return redirect("/watching")


@app.route("/")
@login_required
def index():

    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Invalid username
        if not username:
            flash("Must provide username")
            return render_template("login.html")

        # Invalid password
        elif not password:
            flash("Must provide password")
            return render_template("login.html")

        # Query database
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        print(len(rows))

        # Check if username exists
        if not rows or username != rows[0]["username"]:
            flash("Username doesn't exists.")
            return render_template("login.html")

        # Check if credentials are correct
        elif len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            flash("Invalid username and/or password")
            return render_template("login.html")

        # Log user in
        session["user_id"] = rows[0]["id"]

        # Redirect to home page
        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST
    if request.method == "POST":

        # Check credentials
        if not request.form.get("username"):
            flash("Must provide username")
            return render_template("register.html")

        elif not request.form.get("password"):
            flash("Must provide password")
            return render_template("register.html")

        elif request.form.get("password") != request.form.get("confirm-password"):
            flash("Passwords do not match")
            return render_template("register.html")

        # Enter user
        username = request.form.get("username")
        if not db.execute("SELECT * FROM users WHERE username = ?", username):
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                       username, generate_password_hash(request.form.get("password")))

        else:
            flash("Username already exists")
            return render_template("register.html")

        # Log user in
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    # User reached route via GET
    else:
        return render_template("register.html")


@app.route("/search", methods=["GET", "POST"])
@login_required
def search():
    if request.method == "GET":
        return render_template("search.html")

    else:
        title = request.form.get("name")
        results = lookup(title)

        return render_template("searched.html", results=results)


@app.route("/watched")
@login_required
def watched():

    watchedList = db.execute(
        "SELECT * FROM watched WHERE id = ?", session["user_id"])

    if not watchedList:
        flash("Your list is empty")

    return render_template("watched.html", watchedList=watchedList)


@app.route("/watching")
@login_required
def watching():

    watchingList = db.execute(
        "SELECT * FROM watching WHERE id = ?", session["user_id"])

    if not watchingList:
        flash("Your list is empty")

    return render_template("watching.html", watchingList=watchingList)


@app.route("/favourites")
@login_required
def favourites():

    favouriteList = db.execute(
        "SELECT * FROM favourites WHERE id = ?", session["user_id"])

    if not favouriteList:
        flash("Your list is empty")

    return render_template("favourites.html", favouriteList=favouriteList)

# if __name__ == "__main__":
#     app.run(Debug=True)
