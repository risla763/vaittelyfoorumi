from database import db
from sqlalchemy import text

def get_user_id_by_username(username):
    sql = text("SELECT id FROM users WHERE username = :username")
    result = db.session.execute(sql, {"username": username})

    user = result.fetchone()

    if user:
        return user[0]
    else:
        return None










