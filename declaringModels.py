from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///event_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#initialise database - create a database object
try:
    os.makedirs(app.instance_path)
except OSERROR:
    pass

#defining a model, which represents a table in the database
class Event (db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    date=db.Column(db.DateTime, default=datetime.datetime.utcnow)
    event= db.Column(db.String(200), nullable = False)