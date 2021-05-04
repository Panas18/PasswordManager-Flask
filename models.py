from flask_sqlalchemy import SQLAlchemy
from main import app
from datetime import datetime

db = SQLAlchemy(app)


class User(db.model):
    id = db.column(db.Integer, primary_key=True)
    username = db.column(db.String(120), unique=True, nullable=False)
    email = db.column(db.String(120), unique=True, nullable=False)
    password = db.column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User({self.username}, {self.email})"


class Post(db.model):
    id = db.column(db.Integer, primary_key=True)
    app = db.column(db.String, nullable=False)
    username = db.column(db.String, nullable=False)
    url = db.column(db.String, nullable=False)
    email = db.column(db.String, nullable=False)
    password = db.column(db.String, nullable=False)
    date = db.column(db.DateTime, nullable=False, default = datetime.utcnow)

    def __repr__(self):
        return f"Post({self.app}, {self.username}, {self.email})"
