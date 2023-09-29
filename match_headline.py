from database import db
from sqlalchemy import text

def matching_content(h1):
    sql = text("SELECT headline_id FROM headlines WHERE headline_text = :headline_text")
    result = db.session.execute(sql, {"headline_text": h1})

    headline_id = result.fetchone()
    if headline_id is not None:
 
        sql = text("SELECT message_text, user_id FROM messages1 WHERE headline_id = :headline")
        messages = db.session.execute(sql, {"headline": headline_id[0]})
        messages_list = [(row[0], row[1]) for row in messages.fetchall()]
    else:
         messages_list = []

    for index,(message,user_id) in enumerate(messages_list):
        sql = text("SELECT username FROM users WHERE id = :user_id")
        result = db.session.execute(sql, {"user_id": user_id})
        result = result.scalar()
        tuple = (message,result)
        messages_list[index] = tuple
    print(f"Tämän pitäisi olla hyvä {messages_list}")

    return messages_list

def matching_comment(h1,username,content):
    sql = text("""SELECT
      to_char(timestamp, 'HH24:MI:SS') from messages1;""")
    ####
    sql = text("SELECT headline_id FROM headlines WHERE headline_text = :headline_text")
    result = db.session.execute(sql, {"headline_text": h1})

    headline_id = result.fetchone() #headline id

    sql = text("SELECT id FROM users WHERE username = :username")
    result = db.session.execute(sql, {"username": username})
    user_id = result.fetchone() #user id
    print(content)
    print(user_id)
    print(headline_id)
    sql = text("INSERT INTO messages1 (message_text, user_id, headline_id) "
                "VALUES (:message_text, :user_id, :headline_id)")
    try:
        db.session.execute(sql, {"message_text": content, "user_id": user_id[0], "headline_id": headline_id[0]})
        db.session.commit()
    except Exception as e:
        print("EI ONNISTU")
        db.session.rollback()
#tässä viesti meni messsages1 tietokantaan
    
    if headline_id is not None:
 
        sql = text("SELECT message_text, user_id FROM messages1 WHERE headline_id = :headline")
        messages = db.session.execute(sql, {"headline": headline_id[0]})
        messages_list = [(row[0], row[1]) for row in messages.fetchall()]
    else:
         messages_list = []
    #messages_list tässä kohtaa avain kaikkeen xd!
    for index,(message,user_id) in enumerate(messages_list):
        sql = text("SELECT username FROM users WHERE id = :user_id")
        result = db.session.execute(sql, {"user_id": user_id})
        result = result.scalar()
        tuple = (message,result)
        messages_list[index] = tuple
    print(f"Tämän pitäisi olla hyvä {messages_list}")
    #TÄSTÄ ALKAA TURHA
    #user_message_dict = {}  
    #for message, user_id in messages_list:
        #sql = text("SELECT username FROM users WHERE id = :user_id")
        #result = db.session.execute(sql, {"user_id": user_id})
        #username = result.scalar()
        #if username not in user_message_dict:
            #user_message_dict[username] = []  
        #user_message_dict[username].append(message)
    #print(user_message_dict)
    #TÄHÄN LOPPUU TURHA

    #Tämän jälkeen vielä lista joka yhdistää user_id tosta user_message_dict ja sit users listan käyttäjä nimen
    #ja tee niistä uuusi sanakirja
    return messages_list
