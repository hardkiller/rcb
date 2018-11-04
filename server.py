from flask import Flask,jsonify, json, render_template, send_from_directory, request
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail, Message

import os
import re
import multiprocessing
import datetime


static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'public')

app = Flask(__name__, template_folder='template')

app.config.from_pyfile('config.cfg')

mail = Mail(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@app.route('/')
def root():
    return send_from_directory(static_file_dir, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = os.path.join(path, 'index.html')

    return send_from_directory(static_file_dir, path)


if __name__ == '__main__':
    manager.run()
