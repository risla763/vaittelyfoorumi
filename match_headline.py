from database import db
from sqlalchemy import text


def matching_content(headline_id):
    if headline_id is not None:

        sql = text(
            "SELECT message_text, user_id, answer FROM messages1 WHERE headline_id = :headline")
        messages = db.session.execute(sql, {"headline": headline_id})
        messages_list = [(row[0], row[1], row[2])
                         for row in messages.fetchall()]
    else:
        messages_list = []

    for index, (message, user_id, answer) in enumerate(messages_list):
        sql = text("SELECT username FROM users WHERE id = :user_id")
        result = db.session.execute(sql, {"user_id": user_id})
        result = result.scalar()
        tuple = (message, result, answer)
        messages_list[index] = tuple

    return messages_list


def matching_comment(headline_id, username, content, answer):

    sql = text("SELECT id FROM users WHERE username = :username")
    result = db.session.execute(sql, {"username": username})
    user_id = result.scalar_one()

    sql = text("INSERT INTO messages1 (message_text, user_id, headline_id,answer) "
               "VALUES (:message_text, :user_id, :headline_id, :answer)")
    try:
        db.session.execute(sql, {"message_text": content, "user_id": user_id,
                           "headline_id": headline_id, "answer": answer})
        db.session.commit()
    except Exception as e:
        db.session.rollback()

    if headline_id is not None:

        sql = text(
            "SELECT message_text, user_id, answer FROM messages1 WHERE headline_id = :headline")
        messages = db.session.execute(sql, {"headline": headline_id})
        messages_list = [(row[0], row[1], row[2])
                         for row in messages.fetchall()]
    else:
        messages_list = []

    for index, (message, user_id, answer) in enumerate(messages_list):
        sql = text("SELECT username FROM users WHERE id = :user_id")
        result = db.session.execute(sql, {"user_id": user_id})
        result = result.scalar()
        tuple = (message, result, answer)
        messages_list[index] = tuple

    return messages_list
