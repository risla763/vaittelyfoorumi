from app import app
from flask import render_template, request, redirect, session
import users
import messages
import headlines_to_list 
import match_headline
import profile_information
import started_debates_to_list
import poll_answers_to_db

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
        information = profile_information.profile_information(username)
        started_deb_list = started_debates_to_list.started_debs(username)
        return render_template("profile.html", username=username,information=information,started_debates=started_deb_list)
    else:
        return render_template("error.html", message="Väärä tunnus tai salasana")
    
@app.route("/profile", methods=["POST"])
def profile():
    username = session.get("username")
    started_deb_list = started_debates_to_list.started_debs(username)
    information = profile_information.profile_information(username)
    return render_template("profile.html", username=username,information=information,started_debates=started_deb_list)

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
    answer = request.form["answer"]
    content = request.form["content"]
    headline_text = request.form["headline"]
    poll_answers_to_db.answers_to_db(headline_text,username,answer)
    ##ÄÄÄÄÄÄÄ ONKO TOI YLLÄ OLEVA OIKEINN???? TÄHÄN LASKEE SEN AGREEN percentages = headlines_to_list.count_percentages(headline_text)
    if messages.send(username,content,headline_text,answer):
        return render_template("new_debate.html",username=username,headline=headline_text,content=[content])
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")
    
@app.route("/comment", methods=["POST"])
def comment():
    username = session.get("username")
    content = request.form["content"]
    headline = request.form["headline"]
    answer = request.form["answer"]
    poll = poll_answers_to_db.answers_to_db(headline,username,answer) #täällä kyselyn vastaukset tietokantaan
    messages_list = match_headline.matching_comment(headline,username,content,answer)
    if messages_list:
        return render_template("old_debate.html",headline=headline,messages_list=messages_list,poll=poll)

    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

    
@app.route("/main_page", methods=["GET","POST"])
def main_page():
     return render_template("main_page.html")

@app.route("/headlines_list", methods=["GET","POST"])
def headlines_to_list_route():
    #TÄHÄN SE UUS MUTTA MISTÄ SE REPII NE HEADLINET:::VARMAAN TOSTA ALLA OLEVASTA
    headlines = headlines_to_list.headlines_list() 
    answers = headlines_to_list.count_percentages() #tähän uusi table, johon lisätään myös sama headline kuin headlines ja sen viereen äänestysprosentit..jotka voidaan laskea samassa filessä
    headlines_and_answers = headlines_to_list.combination(headlines,answers)
    if headlines_to_list.headlines_list():
        return render_template("main_page.html",headlines=headlines,answers=answers,combo = headlines_and_answers )
    else:
        return render_template("error.html", message="Ei vielä väittelyitä")
    
@app.route("/old", methods=["GET","POST"])
def fetch_old(): 
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

