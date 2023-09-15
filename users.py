from database import db
from flask import session, request
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    print("hello")
    sql = text("SELECT id, password FROM users WHERE username=:username")
    print("moi")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    print("user")
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username, password):
    username = request.form["username"]
    password = request.form["password"]
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username,password) VALUES (:username,:password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        print("moiiiii")
        return False
    return login(username, password)

def user_id():
    return session.get("user_id",0)