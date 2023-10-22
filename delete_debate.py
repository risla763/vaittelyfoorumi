from markupsafe import escape
from database import db
from sqlalchemy import text


def del_headline(headline_id):
    sql = text(
        " UPDATE headlines SET visible=FALSE WHERE headline_id = :headline_id")
    db.session.execute(sql, {"headline_id": headline_id})
    db.session.commit()
    return True


def del_headline_started(headline_id):
    sql = text(" UPDATE started_debates SET visible=FALSE WHERE id = :headline_id")
    db.session.execute(sql, {"headline_id": headline_id})
    db.session.commit()
    return True
