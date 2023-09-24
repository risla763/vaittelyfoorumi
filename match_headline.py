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
        messages_list = []
    
    user_message_dict = {}  
    for message, user_id in messages_list:
        if user_id not in user_message_dict:
            user_message_dict[user_id] = []
        user_message_dict[user_id].append(message)

    new_dict_for_usernames = {}
    newest_dict={}
    for user_id in user_message_dict.keys():
        sql = text("SELECT username FROM users WHERE id = :user_id")
        result = db.session.execute(sql, {"user_id": user_id})
        result2 = result.fetchone()
        if result2:
            usern = result2[0] #???
            new_dict_for_usernames[user_id] = usern
            newest_dict[usern] = user_message_dict[user_id]
    #Tämän jälkeen vielä lista joka yhdistää user_id tosta user_message_dict ja sit users listan käyttäjä nimen
    #ja tee niistä uuusi sanakirja
    print(f"Tässä tää lista, jossa kaikki: {newest_dict}") 
    return newest_dict

