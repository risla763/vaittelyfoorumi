from markupsafe import escape
from database import db
from un_to_user_id import get_user_id_by_username
from headline_to_db import insert_headline
from sqlalchemy import text  

def send(username, message_text, headline,answer):
    user_id = get_user_id_by_username(username)
    headline_id = insert_headline(headline)
    if user_id is None:
        return False  

    sql = text("INSERT INTO started_debates (username, headline) VALUES (:username, :headline)")
    db.session.execute(sql, {"username": username, "headline": headline})
    db.session.commit() #tässä started_debates username mtchaa kaikkiin debaatteihin..
    #...mitä se user on alottanu
    #print(f"TESTI PÄÄSEEKÖ TÄNNE ASTI {message_text}")
    sql = text("INSERT INTO messages1 (message_text, user_id, headline_id, answer) VALUES (:message_text, :user_id, :headline_id, :answer)")
    try:
        db.session.execute(sql, {"message_text": message_text, "user_id": user_id, "headline_id": headline_id,"answer": answer})
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False


