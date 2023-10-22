from database import db
from un_to_user_id import get_user_id_by_username
from headline_to_db import insert_headline
from sqlalchemy import text  

def answers_to_db(headline_id,username,answer):
    sql = text("INSERT INTO answers (headline_id,username,answer) VALUES (:headline_id, :username, :answer) RETURNING answer")
    result = db.session.execute(sql, {"headline_id": headline_id, "username":username, "answer": answer} )
    db.session.commit()
    result_real = result.fetchone()
    print(f"Tässä on result: {result_real}")
    return result.scalar()

def send(username, message_text, headline,answer):
    user_id = get_user_id_by_username(username)
    headline_id = insert_headline(headline)
    answers_to_db(headline_id,username,answer)
    if user_id is None:
        return False  

    sql = text("INSERT INTO started_debates (username, headline, visible,not_ended) VALUES (:username, :headline, TRUE,TRUE) ")
    db.session.execute(sql, {"username": username, "headline": headline})
    db.session.commit() 
    sql = text("INSERT INTO messages1 (message_text, user_id, headline_id, answer) VALUES (:message_text, :user_id, :headline_id, :answer)")
    try:
        db.session.execute(sql, {"message_text": message_text, "user_id": user_id, "headline_id": headline_id,"answer": answer})
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False



