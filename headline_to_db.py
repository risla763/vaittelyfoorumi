from database import db
from sqlalchemy import text

# Function to insert a headline and return its ID
def insert_headline(headline):
    sql = text("INSERT INTO headlines (headline) VALUES (:headline) RETURNING headline_id")
    
    try:
        result = db.session.execute(sql, {"headline_text": headline})
        db.session.commit()
        return result.scalar()
    except Exception as e:
        db.session.rollback()
        print(f"Error inserting headline: {e}")
        return None