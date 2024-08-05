import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    recipes = mongo.db.recipes.find()
    return render_template('index.html', recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username").lower()
        email = request.form.get("email")
        password = request.form.get("password")
        
        # Check if username or email already exists
        existing_username = mongo.db.users.find_one({"username": username})
        existing_email = mongo.db.users.find_one({"email": email})
        
        if existing_username and existing_email:
            flash("You have already registered, please log in.")
            return redirect(url_for("login")) 
        elif existing_username:
            flash("Username already exists, please choose another username or log in.")
            return redirect(url_for("register")) 
        elif existing_email:
            flash("Email already exists, please log in.")
            return redirect(url_for("register")) 
        
        # Create new user record
        new_user = {
            "username": username,
            "email": email,
            "password": generate_password_hash(password)
        }
        mongo.db.users.insert_one(new_user)
        
        # Set session variable and notify user
        session["user"] = username
        flash("Registration Successful!")
        # change when profile create
        return redirect(url_for("register"))
        
    return render_template('register.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username_or_email = request.form.get("username_or_email").lower()
        password = request.form.get("password")
        
        existing_user = mongo.db.users.find_one({
            "$or": [
                {"username": username_or_email},
                {"email": username_or_email}
            ]
        })
        
        if existing_user:
            if check_password_hash(
                existing_user["password"], password):
                    session["user"] = existing_user["username"]
                    flash("Welcome, {}".format(existing_user["username"]))
                    return redirect(url_for("index"))
            else:
                flash("Incorrect Username/Email and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username/Email and/or Password")
            return redirect(url_for("login"))
        
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)