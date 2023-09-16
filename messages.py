from database import db
from un_to_user_id import get_user_id_by_username
from headline_to_db import insert_headline
from sqlalchemy import text  

def send(username, message_text, headline):
    user_id = get_user_id_by_username(username)
    headline_id = insert_headline(headline)
    print(f"Tämä on user_id: {user_id}") #kovakoodausta
    print(f"Tämä on message_text: {message_text}")
    print(f"Tämä on headline: {headline_id}")
    if user_id is None:
        return False  # Return False if the username is not found

    # Define the SQL statement as text
    sql = text("INSERT INTO messages1 (message_text, user_id, headline_id) "
                "VALUES (:message_text, :user_id, :headline_id)")

    try:
        db.session.execute(sql, {"message_text": message_text, "user_id": user_id, "headline_id": headline_id})
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(f"Error sending message: {e}")
        return False

