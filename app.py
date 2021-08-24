import os
from flask import(
     Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask("__name__")

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"]= os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/travel_stories")
def travel_stories():
    travel_stories= mongo.db.travel_stories.find()
    return render_template("travel_stories.html", travel_stories = travel_stories)


@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if username and email address exist in database
        existing_emailaddress = mongo.db.user_profile.find_one(
            {"emailaddress": request.form.get("emailaddress").lower()})
        if existing_emailaddress:
            flash ("Email address already registered")
            return redirect(url_for("signup"))
        existing_user = mongo.db.user_profile.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash ("Username already exists")
            return redirect(url_for("signup"))
        

        signup = {
            "emailaddress": request.form.get("emailaddress").lower(),
            "username" : request.form.get("username").lower(),
            "password" : generate_password_hash(request.form.get("password"))            
        }
        mongo.db.user_profile.insert_one(signup)

        # put the new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign up successful")
        return redirect(url_for('profile', username=session["user"]))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #check if username exists in db
        existing_user= mongo.db.user_profile.find_one(
            {"username" : request.form.get("username").lower()})

        if existing_user:
            #ensure hased password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                          'profile', username=session["user"]))
            else:
                #invalid password match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))
        else:
            #username does not exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")



@app.route("/profile/<username>", methods = ["GET", "POST"])
def profile(username):
    #grab the sesssion user's username from db
    username = mongo.db.user_profile.find_one({"username": session["user"]})["username"]    
    return render_template("profile.html", username = username)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)