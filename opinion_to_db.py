from database import db
from sqlalchemy import text

def opinions(headline,username,opinion):
    sql = text("INSERT INTO opinions (headline,username,opinion) VALUES (:headline, :username, :opinion) RETURNING opinion")
    result = db.session.execute(sql, {"headline": headline, "username":username, "opinion":opinion} )
    db.session.commit()
    result_real = result.fetchone()
    print(f"Tässä on opinion: {result_real}")
    return result.scalar()