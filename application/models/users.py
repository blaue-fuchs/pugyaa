# -*- coding: utf-8 -*-
import os
from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', "postgresql://tg:tg@127.0.0.1/tgraph")
db = SQLAlchemy(app)


class DBAccess():
    @staticmethod
    def create():
        db.create_all()

    @staticmethod
    def add(table):
        db.session.add(table)
        
    @staticmethod
    def delete(table):
        db.session.add(table)

    @staticmethod
    def commit():
        db.session.commit()

class User(db.Model):
    """
    ユーザ
    """
    user_id = db.Column(db.String(256), primary_key=True)
    token = db.Column(db.String(256))
    secret = db.Column(db.String(256))

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return '<User %r>' % self.user_id

    def update(self, token, secret):
        self.token = token
        self.secret = secret

