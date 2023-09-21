from database import db
from sqlalchemy import text

def headlines_list():
    sql = text("SELECT headline_text FROM headlines")
    data = db.session.execute(sql)

    headlines = [row[0] for row in data.fetchall()] #tekee listan
    print(headlines)
    return headlines