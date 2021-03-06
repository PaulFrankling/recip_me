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


# Home page
@app.route("/")
@app.route("/index")
def index():
    categories = mongo.db.categories.find()
    return render_template("index.html", categories=categories)


# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():
    if not session.get("user"):

        if request.method == "POST":
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                flash("This username already exists!")
                return redirect(url_for("register"))

            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(register)

            session["user"] = request.form.get("username").lower()
            flash("You have successfully registered with RecipMe!")
            return redirect(url_for("profile", username=session["user"]))

    else:
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if not session.get("user"):

        if request.method == "POST":
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                if check_password_hash(
                    existing_user["password"], request.form.get(
                        "password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hello, {}!".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))

                else:
                    flash("Incorrect Username and/or Password!")
                    return redirect(url_for("login"))

            else:
                flash("Incorrect Username and/or Password!")
                return redirect(url_for("login"))

    else:
        return redirect(url_for("profile", username=session["user"]))

    return render_template("login.html")


# Recipes Page
@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    return render_template("recipes.html", recipes=recipes)


# Search Engine for Recipes Page
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# Category Pages
@app.route("/categories/<category_name>")
def categories(category_name):
    categories = mongo.db.categories.find()
    recipes = mongo.db.recipes.find({"category_name": category_name})
    return render_template("categories.html", categories=categories,
                           recipes=recipes, category_name=category_name)


# Show Recipe Page
@app.route("/show_recipe/<recipe_id>")
def show_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients = recipe["recipe_ingredients"]
    methods = recipe["recipe_method"]
    return render_template("show_recipe.html", recipe=recipe,
                           methods=methods, ingredients=ingredients)


# Add Recipe Page
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if not session.get("user"):
        return render_template("404.html")

    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_desc": request.form.get("recipe_desc"),
            "category_name": request.form.get("category_name"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "recipe_method": request.form.getlist("recipe_method"),
            "added_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe successfully added!")
        return redirect(url_for("recipes"))

    categories = mongo.db.categories.find()
    return render_template("add_recipe.html", categories=categories)


# Edit Recipe Page
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if not session.get("user"):
        return render_template("404.html")

    if request.method == "POST":
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_desc": request.form.get("recipe_desc"),
            "category_name": request.form.get("category_name"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "recipe_method": request.form.getlist("recipe_method"),
            "added_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe successfully updated!")
        return redirect(url_for("recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    return render_template("edit_recipe.html",
                           recipe=recipe, categories=categories)


# Delete Function
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted!")
    return redirect(url_for("recipes"))


# Profile Page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if not session.get("user"):
        return render_template("404.html")

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
        return render_template("profile.html",
                               username=username, recipes=recipes)

    return render_template(url_for("login"))


# Logout Function
@app.route("/logout")
def logout():
    flash("You have successfully logged out!")
    session.pop("user")
    return redirect(url_for("login"))


# 404 Error Page
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", error=error), 404


# 500 Error Page
@app.errorhandler(500)
def server_error(error):
    return render_template("500.html", error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
