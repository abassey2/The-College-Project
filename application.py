import os
import csv
import re
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from flask_mail import Mail, Message
from helpers import check

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///collegeproject.db")


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        email = request.form.get("email")
        list = db.execute("SELECT * FROM email_list")
        for row in list:
            if email == row['email']:
                return redirect("/")
        if check(email) == True:
            db.execute("INSERT INTO email_list (name, email) VALUES (?,?)", request.form.get("name"), email)
            return render_template("subscribed.html")
        else:
            return render_template("notsubscribed.html")
    else:
        return render_template("index.html")


@app.route("/learn")
def learn():
    return render_template("learn.html")


@app.route("/racial")
def racial():
    return render_template("racialdiscrimination.html")


@app.route("/orientation")
def orientation():
    return render_template("sexualorientation.html")


@app.route("/assault")
def assault():
    return render_template("sexualassault.html")


@app.route("/donate")
def donate():
    return render_template("donate.html")


@app.route("/share", methods=["GET", "POST"])
def share():
    if request.method == "POST":
        email = request.form.get("email")
        story = request.form.get("story")
        storytype = request.form.get("type")
        name = request.form.get("name")
        if name == '':
            name = "Anonymous"

        if story != '' and check(email) == True and storytype != 'select':
            db.execute("INSERT INTO stories (story, name, email, college, type) VALUES (?,?,?,?,?)",
                       story, name, email, request.form.get("college"), storytype)
            return render_template("shared.html")
        else:
            return render_template("notshared.html")

    else:
        return render_template("share.html")


@app.route("/viewracial", methods=["GET", "POST"])
def viewracial():
    if request.method == "POST":
        keywords = request.form.get("search")
        split_keywords = keywords.split(" ")
        stories = []
        for keyword in split_keywords:
            stories.append(db.execute(
                "SELECT name, college, story FROM stories WHERE type='racial' AND story LIKE ? OR college LIKE ?", '%' + keyword + '%', '%' + keyword + '%'))
        return render_template("viewracial.html", stories=stories)
    else:
        all_stories = []
        all_stories.append(db.execute("SELECT name, college, story FROM stories WHERE type='racial'"))
        return render_template("viewracial.html", stories=all_stories)


@app.route("/vieworientation", methods=["GET", "POST"])
def vieworientation():
    if request.method == "POST":
        keywords = request.form.get("search")
        split_keywords = keywords.split(" ")
        stories = []
        for keyword in split_keywords:
            stories.append(db.execute("SELECT name, college, story FROM stories WHERE type='orientation' AND story LIKE ? OR college LIKE ? OR name LIKE ?",
                                      '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
        return render_template("vieworientation.html", stories=stories)
    else:
        all_stories = []
        all_stories.append(db.execute("SELECT name, college, story FROM stories WHERE type='orientation'"))
        return render_template("vieworientation.html", stories=all_stories)


@app.route("/viewassault", methods=["GET", "POST"])
def viewassault():
    if request.method == "POST":
        keywords = request.form.get("search")
        split_keywords = keywords.split(" ")
        stories = []
        for keyword in split_keywords:
            stories.append(db.execute("SELECT name, college, story FROM stories WHERE type='assault' AND story LIKE ? OR college LIKE ? OR name LIKE ?",
                                      '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
        return render_template("viewassault.html", stories=stories)
    else:
        all_stories = []
        all_stories.append(db.execute("SELECT name, college, story FROM stories WHERE type='assault'"))
        return render_template("viewassault.html", stories=all_stories)


@app.route("/view", methods=["GET", "POST"])
def view():
    if request.method == "POST":
        storytype = request.form.get("type")
        if storytype == 'racial':
            return redirect("/viewracial")
        if storytype == 'orientation':
            return redirect("/vieworientation")
        if storytype == 'assault':
            return redirect("/viewassault")
        return redirect("/")

    else:
        return render_template("view.html")