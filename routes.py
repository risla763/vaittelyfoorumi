from app import app
from flask import render_template, request, redirect
import users


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check username and password
    if users.login(username,password): #tallentaa tietokantaan
        return redirect("/")
    else:
        return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["POST"])
def register():
    print("nyt register")
    username = request.form["username"]
    password = request.form["password"]
    if users.register(username,password):
        return redirect("/")

        