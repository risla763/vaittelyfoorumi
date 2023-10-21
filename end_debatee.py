from database import db
from sqlalchemy import text

def end_debate_headlines_db(headline_id):
    sql = text(" UPDATE headlines SET not_ended=FALSE WHERE headline_id = :headline_id")
    db.session.execute(sql, {"headline_id":headline_id})
    db.session.commit()
    print("APU PRINT",id,)
    return True  
def end_debate_started_headlines_db(headline_id):
    sql = text(" UPDATE started_debates SET not_ended=FALSE WHERE id = :headline_id")
    db.session.execute(sql, {"headline_id":headline_id})
    db.session.commit()
    print("APU PRINT",id,)
    return True

def check_if_ended(headline_id): #uutta
    sql = text("SELECT not_ended FROM headlines WHERE headline_id= :headline_id ")
    result = db.session.execute(sql, {"headline_id":headline_id})
    db.session.commit()
    result = result.scalar()
    print("APU PRINT 1111",result,)
    return result