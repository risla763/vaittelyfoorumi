from app import app
from flask import render_template, request, redirect
import users
import messages


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check username and password
    if users.login(username,password): #tallentaa tietokantaan
        return render_template("new_user_hp.html", username=username)
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
    
@app.route("/new_conversation", methods=["GET","POST"])
def new_conversation():
    return render_template("new_conversation.html")

@app.route("/send", methods=["POST"])
def send():
    print("Meni send")
    #username pitää yhdistää sen user_id koska se on eri asia...ehkä messages filessä..
    username = request.form["username"]
    headline = request.form["headline"]
    content = request.form["content"]
    if messages.send(username,content,headline):
        return render_template("new_debate.html",username=username,headline=headline,content=[content])
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")