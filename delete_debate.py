from markupsafe import escape
from database import db
from sqlalchemy import text  

def del_headline(headline):
    sql = text("SELECT headline_id FROM headlines WHERE headline_text = :headline")
    id = db.session.execute(sql, {"headline":headline})
    id = id.scalar()
    sql = text(" UPDATE headlines SET visible=FALSE WHERE headline_id = :headline_id")
    db.session.execute(sql, {"headline_id":id})
    db.session.commit()
    print("APU PRINT",id,)
    return True

def del_headline_started(headline):
    sql = text("SELECT headline_id FROM headlines WHERE headline_text = :headline")
    id = db.session.execute(sql, {"headline":headline})
    id = id.scalar()
    sql = text(" UPDATE started_debates SET visible=FALSE WHERE id = :headline_id")
    db.session.execute(sql, {"headline_id":id})
    db.session.commit()
    return True