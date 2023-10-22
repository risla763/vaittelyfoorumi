from markupsafe import escape
from app import app
from flask import render_template, request, redirect, session
import secrets
import users
import messages
import search_headline
import headlines_to_list 
import match_headline
import profile_information
import started_debates_to_list
import opinion_to_db
import count_max_messages_db
import delete_debate
import end_debatee

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET", "POST"]) #ÄLÄ MUUTA 
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password): #tallentaa tietokantaan
            session["username"] = username
            information = profile_information.profile_information(username)
            started_deb_list = started_debates_to_list.started_debs(username)
            combo_of_h_a_s_v= profile_information.statement_and_latest_answer(username)
            return render_template("profile.html", username=username,information=information,started_debates=started_deb_list,
            combo_of_h_a_s_v=combo_of_h_a_s_v
                                )
        else:
            return render_template("error.html", message=("L &#129313;"))
    
    return render_template("login_own_page.html")

@app.route("/delete_debate", methods=["GET","POST"])
def del_debate():
    #if request.method == "POST" and session["csrf_token"] != request.form.get("csrf_token"):
        #return render_template("error.html", message=("L &#129313;"))
    username = session.get("username")
    headline_id = request.form["conversation_id"]#tarkista hakeeko?
    #headline_text = str(escape(headline_text)).replace("\r\n", "</br>")
    delete_debate.del_headline(headline_id)
    delete_debate.del_headline_started(headline_id)
    return redirect("/profile")

@app.route("/end_debate", methods=["POST"])
def end_debate():
    headline_id = request.form["conversation_id"]
    end_debatee.end_debate_headlines_db(headline_id)
    end_debatee.end_debate_started_headlines_db(headline_id)

    return redirect("/profile")


@app.route("/result", methods=["GET"])
def search():
    query = request.args["query"]
    search_results = search_headline.search(query)
    #VÄLIAIKAINEN kokeile redirect("/main_page")
    headlines = headlines_to_list.headlines_list() 
    answers = headlines_to_list.count_percentages() 
    opinions = headlines_to_list.opinions_list()
    max_messages = count_max_messages_db.count_max()
    headline_ids = headlines_to_list.headline_ids_list()
    headlines_answers_opinions = headlines_to_list.combination(headlines,answers,opinions,headline_ids)
    return render_template("main_page.html",headlines=headlines,answers=answers,combo = headlines_answers_opinions, max_m = max_messages,results=search_results,queryy=query )
    
@app.route("/profile")
def profile():
    username = session.get("username")
    started_deb_list = started_debates_to_list.started_debs(username)
    information = profile_information.profile_information(username)

    combo_of_h_a_s_v= profile_information.statement_and_latest_answer(username)
    return render_template(
        "profile.html",
        username=username,
        information=information,
        started_debates=started_deb_list,
        combo_of_h_a_s_v=combo_of_h_a_s_v
        )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register_own_page.html")

    username = request.form["username"]
    password = request.form["password"]
    if users.register(username,password):
        return redirect("/")
    else:
        return render_template("error.html", message=(f"This username already exists: {username}"))
    
@app.route("/new_conversation", methods=["GET","POST"])
def new_conversation():
    if request.method == "POST" and session["csrf_token"] != request.form.get("csrf_token"):
        return render_template("error.html", message=("L &#129313;"))
    username = session.get("username")
    return render_template("new_conversation.html", username = username)

@app.route("/send", methods=["POST"]) #Tämä route tärkeä
def send():
    if request.method == "POST" and session.get("csrf_token") != request.form.get("csrf_token"):
        return render_template("error.html", message=("L &#129313;"))
    username = session.get("username")
    answer = str(escape(request.form["answer"])).replace("\r\n", "</br>")
    content = str(escape(request.form["content"])).replace("\r\n", "</br>")
    headline_text = request.form["headline"]
    headline_text = str(escape(headline_text)).replace("\r\n", "</br>")
    statement_short = str(escape(request.form["statement"])).replace("\r\n", "</br>")
    #opinion_to_db.opinions(headline_text,username,statement_short) TURHA
    (headline_text,username,answer)
    if messages.send(username,content,headline_text,answer,statement_short):
        return render_template("new_debate.html",username=username,headline=headline_text,content=[content],statemnt=statement_short)
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")
    
@app.route("/comment", methods=["POST"])
def comment():
    if request.method == "POST" and session["csrf_token"] != request.form.get("csrf_token"):
        return render_template("error.html", message=("L &#129313;"))
    username = session.get("username")
    content = str(escape(request.form["content"]))
    headline_id = request.form["headline_id"]
    headline = request.form["headline"]
    answer = request.form["answer"]
    is_not_ended = True
    poll = messages.answers_to_db(headline_id,username,answer)
    messages_list = match_headline.matching_comment(headline_id,username,content,answer)
    if messages_list:
        return render_template(
            "old_debate.html",
            headline=headline,
            messages_list=messages_list,
            poll=poll,
            is_not_ended=is_not_ended,headline_id=headline_id
            )

    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

    
@app.route("/main_page", methods=["GET","POST"])
def main_page():
     return render_template("main_page.html")

@app.route("/headlines_list", methods=["GET","POST"])
def headlines_to_list_route():
    headlines = headlines_to_list.headlines_list() 
    headline_ids = headlines_to_list.headline_ids_list()
    answers = headlines_to_list.count_percentages() 
    opinions = headlines_to_list.opinions_list()
    max_messages = count_max_messages_db.count_max()
    headlines_answers_opinions = headlines_to_list.combination(headlines,answers,opinions,headline_ids)
    return render_template("main_page.html",headlines=headlines,answers=answers,combo = headlines_answers_opinions, max_m = max_messages )

    
@app.route("/old", methods=["GET","POST"])
def fetch_old(): 
    headline = request.args.get("h1") #tässä pitää periä main_page h1, se josta painetaan linkissä
    headline_id = request.args.get("id") #UUTTA
    is_it_ended = end_debatee.check_if_ended(headline_id) #uuttta
    messages_list = match_headline.matching_content(headline_id)
    if messages_list:
        return render_template("old_debate.html",headline=headline,messages_list=messages_list,is_not_ended=is_it_ended,headline_id=headline_id)
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")
    
@app.route("/logout")
def logout():
    del session["username"]
    return render_template("index.html")

