from app import app
from flask import render_template, request, redirect
import users
import messages
import headlines_to_list 
import match_headline


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

@app.route("/send", methods=["POST"]) #Tämä route tärkeä
def send():
    print("Meni send")
    #username pitää yhdistää sen user_id koska se on eri asia...ehkä messages filessä..
    username = request.form["username"]
    headline_text = request.form["headline"]
    content = request.form["content"]
    print(f"tämä on otsikko:{headline_text}")
    print(request.form)
    if messages.send(username,content,headline_text):
        return render_template("new_debate.html",username=username,headline=headline_text,content=[content])
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")
    
@app.route("/main_page", methods=["GET","POST"])
def main_page():
    print("Etusivullee")
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
    headline = request.args.get("h1") #tässä pitää periä main_page h1, se josta painetaan linkissä
    messages_users_dict = match_headline.matching_content(headline)
    if match_headline.matching_content(headline):
        return render_template("old_debate.html",headline=headline,messages_and_users=messages_users_dict)

    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")
 

        #return render_template("old_debate.html",username=username,content=conten,headline=headline)