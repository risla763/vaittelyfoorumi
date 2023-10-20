from markupsafe import escape
from database import db
from sqlalchemy import text

def insert_headline(headline):
    sql = text("INSERT INTO headlines (headline_text,visible) VALUES (:headline,TRUE) RETURNING headline_id")
    #TÄNNE LISÄÄTY PERJANATINA VISIBLE
    try:
        result = db.session.execute(sql, {"headline": headline})
        db.session.commit()
        return result.scalar()
    except Exception as e:
        db.session.rollback()
        return None