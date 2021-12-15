# from flask import Response, request
from flask_sqlalchemy import SQLAlchemy
# import json


db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Masterpiece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    company = db.Column(db.String(255))
    image = db.Column(db.String(255))
    authors = db.Column(db.String(255), nullable=False)