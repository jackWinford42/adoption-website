"""Models for Adopt."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

default_url = "https://bit.ly/3y8O4Be"

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False, default=default_url)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

def connect_db(app):
    """Connect to database."""
    
    db.app = app
    db.init_app(app)