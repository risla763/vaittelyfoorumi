from database import db
from sqlalchemy import text

def matching_content(h1):
    print(h1)
    sql = text("SELECT headline_id FROM headlines WHERE headline_text = :headline_text")
    result = db.session.execute(sql, {"headline_text": h1})

    headline_id = result.fetchone()
    if headline_id is not None:
        print(headline_id)

        sql = text("SELECT message_text, user_id FROM messages1 WHERE headline_id = :headline")
        messages = db.session.execute(sql, {"headline": headline_id[0]})
        messages_list = [(row[0], row[1]) for row in messages.fetchall()]
        print(f"TÄSSÄ LISTA: {messages_list}")
    else:
        print("Error")

    user_message_dict = {}  
    for message, user_id in messages_list:
        if user_id not in user_message_dict:
            user_message_dict[user_id] = []
        user_message_dict[user_id].append(message)

    return user_message_dict 


