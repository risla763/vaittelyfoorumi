from database import db
from sqlalchemy import text

def started_debs(username):
    sql = text("SELECT headline,id FROM started_debates WHERE username = :username AND visible = TRUE order by id")
    debates = db.session.execute(sql, {"username": username})

    started_deb_headlines = [row for row in debates.fetchall()] 
    if started_deb_headlines == []:
        return None
    return started_deb_headlines
