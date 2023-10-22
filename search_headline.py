from database import db
from sqlalchemy import text


def search(query):
    sql = text(
        "SELECT headline_text,headline_id FROM headlines WHERE headline_text LIKE :query AND visible=TRUE")
    result = db.session.execute(sql, {"query": "%"+query+"%"})
    search_results = result.fetchall()
    return search_results
