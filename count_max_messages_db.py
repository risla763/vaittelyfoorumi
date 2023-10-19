from database import db
from sqlalchemy import text

def count_max():
    sql = text("SELECT headline_id, COUNT(*) AS messages_count FROM messages1 GROUP BY headline_id")
    result = db.session.execute(sql).fetchall()
    result = result if result else [] #tähän tein korjauksen
    max = 0
    max_id = 0
    for i in result:
        if i[1] > max:
            max = i[1]
            max_id = i[0]
    if max_id != 0 and max_id is not None:
        sql = text("SELECT headline_text FROM headlines WHERE headline_id = :max_id")
        max_headline = db.session.execute(sql.bindparams(max_id=max_id))
        max_id = [i[0] for i in max_headline.fetchall()]
        max_tuple = (max_id,max)
        return max_tuple
    else:
        return max
