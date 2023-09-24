from database import db
from sqlalchemy import text

def insert_headline(headline):
    print((f"tämä on HEADLINE:{headline}"))
    sql = text("INSERT INTO headlines (headline_text) VALUES (:headline) RETURNING headline_id")
    
    try:
        result = db.session.execute(sql, {"headline": headline})
        db.session.commit()
        return result.scalar()
    except Exception as e:
        db.session.rollback()
        print(f"Error inserting headline: {e}")
        return None