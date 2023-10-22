from database import db
from sqlalchemy import text

def count_the_votes():
    sql = text("SELECT answer, COUNT(answer) AS count FROM answers WHERE answer IN ('agree', 'disagree') GROUP BY answer")
    result = db.session.execute(sql)
    result = result.fetchone()