from database import db
from sqlalchemy import text

def end_debate_headlines_db(headline_id):
    sql = text(" UPDATE headlines SET not_ended=FALSE WHERE headline_id = :headline_id")
    db.session.execute(sql, {"headline_id":headline_id})
    db.session.commit()
    return True  
def end_debate_started_headlines_db(headline_id):
    sql = text(" UPDATE started_debates SET not_ended=FALSE WHERE id = :headline_id")
    db.session.execute(sql, {"headline_id":headline_id})
    db.session.commit()
    return True

def check_if_ended(headline_id):
    sql = text("SELECT not_ended FROM headlines WHERE headline_id= :headline_id order by headline_id")
    result = db.session.execute(sql, {"headline_id":headline_id})
    db.session.commit()
    result = result.scalar()
    return result