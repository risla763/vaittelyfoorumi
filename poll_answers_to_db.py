from database import db
from sqlalchemy import text

def answers_to_db(headline,username,answer):
    sql = text("INSERT INTO answers (headline,username,answer) VALUES (:headline, :username, :answer) RETURNING answer")
    result = db.session.execute(sql, {"headline": headline, "username":username, "answer":answer} )
    db.session.commit()
    result_real = result.fetchone()
    print(f"Tässä on result: {result_real}")
    return result.scalar()

