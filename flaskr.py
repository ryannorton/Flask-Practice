from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import sqlite3

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'djangoandflaskbattleitout'
USERNAME = 'admin'
PASSWORD = 'default'

# the meat n bones
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
	app.run()