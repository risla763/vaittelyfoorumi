from flask import Flask
from os import getenv
from database import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///maija'
db.init_app(app)

import routes

