#GERSON NAO ESQUECE DE TIRAR O DEBUG=TRUE PARA FALSE ANTES DE ENTREGAR O PROJETO
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
def home():
    return render_template ("home.html")
def register():
    return render_template("register.html")


@app.route("/get_ingredients")
def get_ingredients():
    ingredients = mongo.db.ingredients.find()
    return render_template ("ingredients.html", ingredients=ingredients)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe": request.form.get("recipe"),
            "ingredients": request.form.get("ingredients"),
            "cooking": request.form.get("cooking"),
            "username": session["user"]
        }

        mongo.db.ingredients.insert_one(recipe)
        flash("Task Successfully Added")
        return profile(session["user"])

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("new_recipe.html", categories=categories)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the recipe user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        ingredients = mongo.db.ingredients.find({"username": session["user"]})
        return render_template("profile.html", username=username, ingredients=ingredients)

    return redirect(url_for("login"))


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.ingredients.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return profile(session["user"])


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)