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
            # change when login create
            return redirect(url_for("register")) 
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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)