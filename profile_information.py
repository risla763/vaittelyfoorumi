from database import db
from sqlalchemy import text

def profile_information(username):
    sql = text("SELECT id FROM users WHERE username =:username")
    user_id_1 = db.session.execute(sql, {"username": username})
    user_id = user_id_1.scalar()

    sql = text("SELECT headline_id FROM messages1 WHERE user_id =:user_id" )
    headline_id_1 = db.session.execute(sql, {"user_id": user_id})
    headline_id = headline_id_1.fetchall()
    headline_id_list = [i[0] for i in headline_id]
    help_list = []
    #print(f"HEADLINE ID:S {headline_id_list}")
    for i in headline_id_list:
        if i in help_list or i == None:
            continue
        else:
            help_list.append(i)
    #print(f"LOPULLINEN {help_list}")
    help_list_2 = []
    for i in help_list:
        sql = text("SELECT headline_text FROM headlines WHERE headline_id =:headline_id")
        result = db.session.execute(sql, {"headline_id":i})
        headline = result.scalar()
        help_list_2.append(headline)
        print(f"TESTIII {help_list_2}")
    return help_list_2

