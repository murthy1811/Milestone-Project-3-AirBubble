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
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


#  collects all stories and add to html
@app.route("/")
@app.route("/travel_stories")
def travel_stories():
    travel_stories = list(mongo.db.travel_stories.find())
    return render_template(
        "travel_stories.html", travel_stories=travel_stories)


# search the stories and return results from db
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    travel_stories = list(
        mongo.db.travel_stories.find({"$text": {"$search": query}}))
    return render_template(
        "travel_stories.html", travel_stories=travel_stories)


# sign up functionality
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if username and email address exist in database
        existing_emailaddress = mongo.db.user_profile.find_one(
            {"emailaddress": request.form.get("emailaddress").lower()})
        if existing_emailaddress:
            flash("Email address already registered")
            return redirect(url_for("signup"))
        existing_user = mongo.db.user_profile.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))
        signup = {
            "emailaddress": request.form.get("emailaddress").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
            }
        mongo.db.user_profile.insert_one(signup)

        # put the new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign up successful")
        return redirect(url_for('profile', username=session["user"]))

    return render_template("signup.html")


# login functionality
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.user_profile.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                     existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    'profile', username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


# logged user profile display
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the sesssion user's username from db
    username = mongo.db.user_profile.find_one(
        {"username": session["user"]})["username"]
    emailaddress = mongo.db.user_profile.find_one(
        {"username": session["user"]})["emailaddress"]
    travel_stories = list(mongo.db.travel_stories.find())

    if session["user"]:
        return render_template(
            "profile.html", username=username, emailaddress=emailaddress,
            travel_stories=travel_stories)
    return redirect(url_for('login'))


# change password functionality
@app.route("/changePassword/<username>", methods=["GET", "POST"])
def changePassword(username):
    if request.method == "POST":
        # grab the current user session
        current_user = mongo.db.user_profile.find_one(
            {"username": session["user"]})
        update_password = generate_password_hash(
            request.form.get("newPassword"))
        # check if entered current password and db password match
        if check_password_hash(current_user["password"],
                               request.form.get("currentPassword")):
            mongo.db.user_profile.update(
                {"username": session["user"]},
                {"$set": {"password": update_password}})
            flash("Your Password Updated Successfully")
        else:
            flash("Your current Password does not match with records")
        return redirect(url_for('profile', username=session["user"]))


# logout functionality for session user
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for('login'))


# adding travel story by session user
@app.route("/add_story", methods=["GET", "POST"])
def add_story():
    if request.method == "POST":
        travelstory = {
            "category_name": request.form.get("category_name"),
            "origin": request.form.get("originAirportCode"),
            "origin_country": request.form.get("originCountry"),
            "transit": request.form.get("transitAirportCode"),
            "transit_country": request.form.get("transitCountry"),
            "destination": request.form.get("destinationAirportCode"),
            "destination_country": request.form.get("destinationCountry"),
            "date_of_journey": request.form.get("dateOfJourney"),
            "no_of_adults": request.form.get("noOfAdults"),
            "kids_under_12": request.form.get("kidsUnder12"),
            "kids_under_6": request.form.get("kidsUnder6"),
            "covid_report": request.form.get("covidReport"),
            "your_experience": request.form.get("experience"),
            "added_by": session["user"]
            }
        mongo.db.travel_stories.insert_one(travelstory)
        flash("Your Travel Story is added successfully")
        return redirect(url_for("travel_stories"))

    category = mongo.db.category.find().sort("category_name", -1)
    return render_template("add_story.html", category=category)


# edit travel story by session user
@app.route("/edit_story/<story_id>", methods=["GET", "POST"])
def edit_story(story_id):
    if request.method == "POST":
        submitstory = {
            "category_name": request.form.get("category_name"),
            "origin": request.form.get("originAirportCode"),
            "origin_country": request.form.get("originCountry"),
            "transit": request.form.get("transitAirportCode"),
            "transit_country": request.form.get("transitCountry"),
            "destination": request.form.get("destinationAirportCode"),
            "destination_country": request.form.get("destinationCountry"),
            "date_of_journey": request.form.get("dateOfJourney"),
            "no_of_adults": request.form.get("noOfAdults"),
            "kids_under_12": request.form.get("kidsUnder12"),
            "kids_under_6": request.form.get("kidsUnder6"),
            "covid_report": request.form.get("covidReport"),
            "your_experience": request.form.get("experience"),
            "added_by": session["user"]
            }
        mongo.db.travel_stories.update(
            {"_id": ObjectId(story_id)}, submitstory)
        flash("Your Travel Story is updated successfully")
    story = mongo.db.travel_stories.find_one({"_id": ObjectId(story_id)})
    category = mongo.db.category.find().sort("category_name", -1)
    return render_template("edit_story.html", story=story, category=category)


# readmore page for each travel story
@app.route("/read_more/<story_id>", methods=["GET", "POST"])
def read_more(story_id):
    travel_stories = list(mongo.db.travel_stories.find(
        {"_id": ObjectId(story_id)}))
    comments = list(mongo.db.user_comments.find(
        {"linked_travel_id": ObjectId(story_id)}))
    return render_template(
            "read_more.html", travel_stories=travel_stories, comments=comments)


# comments functionality
@app.route("/comments/<story_id>", methods=["GET", "POST"])
def comments(story_id):
    linked_travelstory = ObjectId(story_id)
    if request.method == "POST":
        usercomment = {
            "comment": request.form.get("comment"),
            "linked_travel_id":  linked_travelstory,
            "commenter": request.form.get("user")
        }
        mongo.db.user_comments.insert_one(usercomment)
        return redirect(url_for('read_more', story_id=story_id))


# delete comments functionality by session user
@app.route("/delete_comment/<comment_id>,<story_id>")
def delete_comment(comment_id, story_id):
    mongo.db.user_comments.remove({"_id": ObjectId(comment_id)})
    flash("Comment is successfully deleted")
    return redirect(url_for('read_more', story_id=story_id))


# delete story functionality by session user
@app.route("/delete_story/<story_id>")
def delete_story(story_id):
    mongo.db.travel_stories.remove({"_id": ObjectId(story_id)})
    mongo.db.user_comments.remove({"linked_travel_id": ObjectId(story_id)})
    flash("Your Travel Story is successfully deleted")
    return redirect(url_for('profile', username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(
        os.environ.get("PORT")), debug=False)
