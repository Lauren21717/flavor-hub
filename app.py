import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for, abort, jsonify)
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


# Index page
@app.route("/")
@app.route("/index")
def index():
    """
    Renders the homepage with a list of all recipes.
    """
    recipes = list(mongo.db.recipes.find())
    return render_template('index.html', recipes=recipes)


#Search Bar
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Searches the recipes based on the query provided by the user.
    """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template('index.html', recipes=recipes)


#Register Page
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Registers a new user and stores their information in the database.
    Checks for existing username or email before registration.
    """
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
        return redirect(url_for("profile", username=session["user"]))
        
    return render_template('register.html')


#Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Logs in an existing user by checking the username/email and password.
    """
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
                    return redirect(url_for("profile", username=session["user"]))
            else:
                flash("Incorrect Username/Email and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username/Email and/or Password")
            return redirect(url_for("login"))
        
    return render_template("login.html")


#Profile Page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Displays the profile page of the logged-in user along with their created recipes.
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        user_recipes = list(mongo.db.recipes.find({"created_by": session["user"]}))
        return render_template("profile.html", username=username, user_recipes=user_recipes)

    return redirect(url_for("login"))


#Logout functionality
@app.route("/logout")
def logout():
    """
    Logs out the current user by clearing the session and redirects to the login page.
    """
    # Code copied from Mini Project | Putting It All Together tutorial at https://learn.codeinstitute.net/
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


#Add recipe page
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Allows users to add a new recipe to the database. 

    Handles recipe creation by collecting form data and inserting it into the MongoDB collection 'recipes'.
    Redirects to the index page upon successful addition. Displays a 500 error page if an issue occurs.
    """
    try:
        if request.method == "POST":
            ingredients = request.form.getlist("ingredients")
            preparation_step = request.form.getlist("preparation_step")
            
            recipe = {
                "category_name": request.form.get("category_name"),
                "recipe_title": request.form.get("recipe_title"),
                "cuisine": request.form.get("cuisine"),
                "preparation_time": request.form.get("preparation_time"),
                "cook_time": request.form.get("cook_time"),
                "image_url": request.form.get("image_url"),
                "ingredients": [ingredient.strip() for ingredient in ingredients],
                "preparation_step": [step.strip() for step in preparation_step],
                "created_by": session["user"]
            }
            mongo.db.recipes.insert_one(recipe)
            flash("Recipe Successfully Added")
            return redirect(url_for("index"))
        
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("add_recipe.html", categories=categories)
    
    except Exception as e:
        app.logger.error(f"Error adding recipe: {e}")
        flash("An error occurred while adding the recipe. Please try again later.")
        return redirect(url_for("add_recipe"))


#Edit Recipe Page
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Allows a logged-in user to edit an existing recipe.
    """
    if request.method == "POST":
        ingredients = request.form.getlist("ingredients")
        preparation_step = request.form.getlist("preparation_step")
        
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_title": request.form.get("recipe_title"),
            "cuisine": request.form.get("cuisine"),
            "preparation_time": request.form.get("preparation_time"),
            "cook_time": request.form.get("cook_time"),
            "image_url": request.form.get("image_url"),
            "ingredients": [ingredient.strip() for ingredient in ingredients],
            "preparation_step": [step.strip() for step in preparation_step],
            "created_by": session["user"]
        }
        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)},
            {"$set": submit})
        flash("Recipe Successfully Updated")
    
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)


#Delete recipe functionality
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Allows a logged-in user to delete a recipe they created.
    """
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})  
    return jsonify({"success": True, "message": "Recipe successfully deleted"})


#Admin Page Get Categories and Users functionality
@app.route("/admin_dashboard")
def admin_dashboard():
    """
    Renders the categories management page, accessible only by "admin".
    """
    current_user = mongo.db.users.find_one({"username": session["user"]})
    
    if current_user and current_user["username"] == "admin":
        all_users = mongo.db.users.find()
        categories = list(mongo.db.categories.find().sort("category_name", 1))
        return render_template("admin_dashboard.html", categories=categories, all_users = all_users)

    abort(403)


#Admin Page Add Categories functionality
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    Allows "admin" to add a new category to the database.
    """
    current_user = mongo.db.users.find_one({"username": session["user"]})
    
    if current_user and current_user["username"] == "admin":
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name")
            }
            mongo.db.categories.insert_one(category)
            flash("New Category Added")
            return redirect(url_for("admin_dashboard"))
        
        return render_template("add_category.html")

    abort(403)


#Admin Page Edit Categories functionality
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    Allows "admin" to edit an existing category.
    """
    current_user = mongo.db.users.find_one({"username": session["user"]})
    
    if current_user and current_user["username"] == "admin":
        if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name")
            }
            mongo.db.categories.update_one({"_id": ObjectId(category_id)}, {"$set": submit})
            flash("Category Updated")
            return redirect(url_for("admin_dashboard"))
        
        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
        return render_template("edit_category.html", category=category)

    abort(403)


#Admin Page Delete Categories functionality
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    Allows "admin" to delete an existing category.
    """
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("admin_dashboard"))

#Admin Page Delete User functionality
@app.route("/delete_user/<user_id>", methods=["POST"])
def delete_user(user_id):
    """
    Allows "admin" to delete a user and all their associated recipes.
    """
    current_user = mongo.db.users.find_one({"username": session["user"]})
    
    if current_user and current_user["username"] == "admin":
        user_to_delete = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        
        if user_to_delete and user_to_delete["username"] != "admin":
            # Delete all recipes created by this user
            mongo.db.recipes.delete_many({"created_by": user_to_delete["username"]})
            
            # Delete the user
            mongo.db.users.delete_one({"_id": ObjectId(user_id)})
            
            flash(f"User {user_to_delete['username']} and all their recipes have been deleted")
        else:
            flash("Cannot delete admin user or user not found")
        
        return redirect(url_for("admin_dashboard"))
    
    abort(403)


#Recipe Page
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    """
    Retrieves and displays details of a specific recipe.
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    
    if not recipe:
        abort(404)
    
    return render_template("recipe.html", recipe=recipe)


#404
@app.errorhandler(404)
def page_not_found(e):
    """
    Renders the 404 error page when the requested resource is not found.
    """
    return render_template('404.html'), 404


#403
@app.errorhandler(403)
def forbidden(e):
    """
    Renders the 403 error page when the user is not authorized to access the resource.
    """
    return render_template('403.html'), 403


#500
@app.errorhandler(500)
def internal_server(e):
    """
    Renders the 500 error page when there is an internal server error.
    """
    return render_template('500.html'), 500


#Contact
@app.route("/contact", methods=["GET"])
def contact():
    """
    Renders the contact page
    """
    email_api = os.environ.get("EMAIL_API")
    return render_template("contact.html", email_api=email_api)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)