from database import db
from sqlalchemy import text

def count_max():
    sql = text("SELECT headline_id, COUNT(*) AS messages_count FROM messages1 GROUP BY headline_id")
    result = db.session.execute(sql).fetchall()
    print(f"MOII TÄSSÄ RESULT {result}")
    max = 0
    for i in result:
        if i[1] > max:
            max = i[1]
            max_id = i[0]
    print(f"MOII TÄSSÄ maxxx {max}")
    if max_id is not None:
        sql = text("SELECT headline_text FROM headlines WHERE headline_id = :max_id")
        max_headline = db.session.execute(sql.bindparams(max_id=max_id))
        max_id = [i[0] for i in max_headline.fetchall()]
        print(f"MOII TÄSSÄ maxxx {max}")
        max_tuple = (max_id,max)
        return max_tuple
    else:
        return None
