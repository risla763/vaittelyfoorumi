from database import db
from sqlalchemy import text

def search(query):
    sql = text("SELECT headline_text FROM headlines WHERE headline_text LIKE :query")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    search_results = result.fetchall()
    print("search results",search_results)
    return search_results