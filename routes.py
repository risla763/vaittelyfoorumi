from app import app
from flask import render_template, request, redirect, session
import users
import messages
import headlines_to_list 
import match_headline


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"]) #ÄLÄ MUUTA 
def login():
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check username and password
    if users.login(username,password): #tallentaa tietokantaan
        session["username"] = username
        return render_template("new_user_hp.html", username=username)
    else:
        return render_template("error.html", message="Väärä tunnus tai salasana")
    
@app.route("/login_page", methods= ["GET","POST"])
def login_page():
    return render_template("login_own_page.html")

@app.route("/register_page", methods= ["GET", "POST"])
def register_page():
    return render_template("register_own_page.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    if users.register(username,password):
        return redirect("/")
    else:
        return render_template("error.html", message=(f"This username already exists: {username}"))
    
@app.route("/new_conversation", methods=["GET","POST"])
def new_conversation():
    username = session.get("username")
    return render_template("new_conversation.html", username = username)

@app.route("/send", methods=["POST"]) #Tämä route tärkeä
def send():
     #username pitää yhdistää sen user_id koska se on eri asia...ehkä messages filessä..
    username = session.get("username")
    #username = request.form["username"]
    content = request.form["content"]
    headline_text = request.form["headline"]
    if messages.send(username,content,headline_text):
        return render_template("new_debate.html",username=username,headline=headline_text,content=[content])
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")
    
@app.route("/comment", methods=["POST"])
def comment():
    username = session.get("username")
    content = request.form["content"]
    headline = request.form["headline"]
    messages_list = match_headline.matching_comment(headline,username,content)
    if messages_list:
        return render_template("old_debate.html",headline=headline,messages_list=messages_list)

    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

    
@app.route("/main_page", methods=["GET","POST"])
def main_page():
     return render_template("main_page.html")

@app.route("/headlines_list", methods=["GET","POST"])
def headlines_to_list_route():
    headlines = headlines_to_list.headlines_list()
    if headlines_to_list.headlines_list():
        return render_template("main_page.html",headlines=headlines)
    else:
        return render_template("error.html", message="Ei vielä väittelyitä")
    
@app.route("/old", methods=["GET","POST"])
def fetch_old():
    print("moro moro")  
    headline = request.args.get("h1") #tässä pitää periä main_page h1, se josta painetaan linkissä
    messages_list = match_headline.matching_content(headline)
    if messages_list:
        return render_template("old_debate.html",headline=headline,messages_list=messages_list)
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")
    
@app.route("/logout")
def logout():
    del session["username"]
    return render_template("index.html")

