#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-

import flask
import flask.ext.sqlalchemy
import flask.ext.restless
from datetime import datetime

app = flask.Flask(__name__)
app.config.from_pyfile('settings.py')
db = flask.ext.sqlalchemy.SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode)
    description = db.Column(db.Unicode)
    create_date = db.Column(db.DateTime, default=datetime.now())
    deadline = db.Column(db.DateTime)
    done = db.Column(db.Boolean, default=False)

db.create_all()

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(
    Task, methods=['GET', 'POST', 'PATCH', 'DELETE'], results_per_page=20)

if __name__ == '__main__':
    app.run()
