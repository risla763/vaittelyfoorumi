from database import db
from sqlalchemy import text

def started_debs(username):
    sql = text("SELECT headline FROM started_debates WHERE username = :username")
    debates = db.session.execute(sql, {"username": username})

    started_deb_headlines = [row[0] for row in debates.fetchall()] #tekee listan
    return started_deb_headlines
