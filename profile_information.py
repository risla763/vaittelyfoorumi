from database import db
from sqlalchemy import text
#Tähän tee että jos väittelyllä
def profile_information(username):
    sql = text("SELECT id FROM users WHERE username =:username")
    user_id_1 = db.session.execute(sql, {"username": username})
    user_id = user_id_1.scalar()

    sql = text("SELECT headline_id FROM messages1 WHERE user_id =:user_id" )
    headline_id_1 = db.session.execute(sql, {"user_id": user_id})
    headline_id = headline_id_1.fetchall()
    headline_id_list = [i[0] for i in headline_id]
    headline_id_list_true = []
    for id in headline_id_list:
        sql = text("SELECT 1 FROM headlines WHERE headline_id = :headline_id AND visible = TRUE")

        result = db.session.execute(sql, {"headline_id": id}).scalar()
        if result == 1:
            print("MIKÄ TÄÄ ON", id)
            headline_id_list_true.append(id)


    #yllä uutta^^^^^^
    help_list = []
    if headline_id_list == []:
        return None
    for i in headline_id_list_true:
        if i in help_list or i == None:
            continue
        else:
            help_list.append(i)
    print(f"LOPULLINEN {help_list}")
    ##TÄSSÄ KATO ONKO HELP_LISTISSÄ SE FALSE VAI TRUE
    help_list_2 = []
    for i in help_list:
        sql = text("SELECT headline_text FROM headlines WHERE headline_id =:headline_id")
        result = db.session.execute(sql, {"headline_id":i})
        headline = result.scalar()
        help_list_2.append(headline)
    return help_list_2

def latest_answers_per_user(username):
    sql = text("SELECT id FROM users WHERE username= :username")
    result = db.session.execute(sql, {"username":username})
    headline_list = profile_information(username)
    result = result.fetchone()
    result = result[0]
    print(f"result{result}")
    ans_headline = []
    print(f"result{headline_list}")
    if headline_list: #TÄMÄN PITÄISI TARKISTAA ONKO USER_ID OSALLISTUNUT YHTEENKÄÄN VÄITTELYYN
        
        user_id = result
        for headline in headline_list:
            #
            sql = text("SELECT h.headline_id"
                       " FROM messages1 m JOIN headlines h ON m.headline_id = h.headline_id"
                       " WHERE h.headline_text = :headline AND h.visible = TRUE")
            headline_id = db.session.execute(sql, {"headline":headline})
            db.session.commit()
            headline_id = headline_id.fetchall()
            if headline_id:
                print("TÄSSÄ HEADLINE_ID", headline_id)
                if headline_id:
                    print("TÄSSÄ HEADLINE_ID", headline_id[0][0]) #tämä toimii ##TÄMÄ LISTA TÄSSÄ HEADLINE_ID [(1,), (1,), (1,), (1,), (1,)] ja headline_id[0]=(1,) NIISTÄ MUTTA LAITA ETTÄ NE ON SORTED JA JOS ON SAMA KAHTEEN KERTAAN NIII DELETE NII TÄSSÄ ON ID LISTA
                #if headline_id == []:
                    #return None #Jos ei oo debaatteja
                headline_id = headline_id[0][0]
                sql = text("SELECT answer FROM messages1 WHERE headline_id = :headline_id AND user_id = :user_id ORDER BY timestamp DESC LIMIT 1;")
                result = db.session.execute(sql, {"user_id":user_id, "headline_id":headline_id})
                answer = result.scalar()
                db.session.commit()
                tuple = (headline,answer)
                ans_headline.append(tuple)
                print("Latest answer:", ans_headline)
                #TÄHÄN LISTA HEADLINE_ID JA SEN USERNAMEN ANSWER
        return ans_headline
    return None

def statement_and_latest_answer(username):
    tuple_h_a = latest_answers_per_user(username)
    tuple_h_a = tuple_h_a if tuple_h_a else []
    list_of_statements = []
    x = 0
    #tässä tee uus lista 
    for i in tuple_h_a:
        print("lollll",tuple_h_a[0])
        sql = text("SELECT opinion FROM opinions WHERE headline = :headline")
        statement = db.session.execute(sql,{"headline":tuple_h_a[x][0]})
        #tuple jossa on kolme kohtaa
        db.session.commit()
        statement = statement.fetchone()
        list_of_statements.append(statement)
        x += 1
    headline_id_list = just_headline_id_list(username) #POISTA
    print("statement:", list_of_statements)
    print("TUPLE:",  tuple_h_a)
    print("VALUE:",  tuple_h_a)
    combination_of_h_a_s_v = []
    for tuple, statement,id in zip(tuple_h_a,list_of_statements,headline_id_list):
        if statement is not None:
            print("ID LOOPIN SISÄLLÄ:",  tuple_h_a)
            combination_of_h_a_s_v.append({'headline': tuple[0], 'opinion': tuple[1], 'statement':statement[0], 'headline_id':id})
        else:
            combination_of_h_a_s_v.append({'headline': tuple[0], 'opinion': tuple[1], 'statement':statement,'headline_id':id})
    print("Latest answer:",combination_of_h_a_s_v )
    if combination_of_h_a_s_v == []:
        return None
    return combination_of_h_a_s_v

def just_headline_id_list(username): #UUTTA EHKÄ POISTA
    sql = text(
        """
        SELECT DISTINCT m.headline_id 
        FROM messages1 m
        inner join users u on m.user_id = u.id 
        inner join headlines h on h.headline_id = m.headline_id
        WHERE username =:username
        AND h.visible=TRUE
        """)
    headline_id = db.session.execute(sql, {"username": username}).fetchall()
    return [i[0] for i in headline_id ]
            