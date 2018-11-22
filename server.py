from flask import Flask, jsonify, json, render_template, send_from_directory, request
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


class BaseJournalingFields(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer)

    name = db.Column(db.String(255))
    code = db.Column(db.String(255))

    description = db.column(db.Text)
    comment = db.column(db.Text)

    create_user_id = db.Column(db.Integer)
    create_datetime = db.Column(db.DateTime)

    update_user_id = db.Column(db.Integer)
    update_datetime = db.Column(db.DateTime)

    delete_user_id = db.Column(db.Integer)
    delete_datetime = db.Column(db.DateTime)

    discriminator = db.Column('type', db.String(50))
    __mapper_args = {'polymorphic_on': discriminator}


class Resource(BaseJournalingFields):
    __tablename__ = 'resource'


class MeasureType(Resource):

    symbol_en = db.Column(db.String(50))
    symbol_ru = db.Column(db.String(50))

    __mapper_args__ = {'polymorphic_identity': 'measure_type'} 


class ElementType(Resource):
    __mapper_args__ = {'polymorphic_identity': 'element_type'}


class StoreRack(Resource):
    __mapper_args__ = {'polymorphic_identity': 'store_rack'}


class Element(Resource):
    __mapper_args__ = {'polymorphic_identity': 'element'}


class GrantType(Resource):
    __mapper_args__ = {'polymorphic_identity': 'grant_type'}


class ElementProperty(Resource):

    __tablename__ = 'element_property'
    __mapper_args__ = {'polymorphic_identity': 'element_property'}

    id = db.Column('id', db.Integer, db.ForeignKey('resource.id'), primary_key=True)

    element_id = db.Column(db.Integer)
    measure_type_id = db.Column(db.Integer)
    value_type = db.Column(db.String(50))
    value_range_min = db.Column(db.Float)
    value_range_max = db.Column(db.Float)
    value_text = db.column(db.Text)
    value_integer = db.column(db.Integer)
    value_float = db.column(db.Float)
 

class User(Resource):

    __tablename__ = 'user'
    __mapper_args__ = {'polymorphic_identity': 'user'}

    id = db.Column('id', db.Integer, db.ForeignKey('resource.id'), primary_key=True)

    login = db.Column(db.String(255))
    passwd_hash = db.Column(db.String(255))
    email = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))


class UserGrant(Resource):

    __tablename__ = 'user_grant'
    __mapper_args__ = {'polymorphic_identity': 'user_grant'}

    id = db.Column('id', db.Integer, db.ForeignKey('resource.id'), primary_key=True)

    user_id = db.Column(db.Integer)
    grant_type_id = db.Column(db.Integer)
    access_allowed = db.Column(db.Boolean)
 

class Assembly(BaseJournalingFields):
    __tablename__ = 'assembly'


class AssemblyElement(Assembly):

    __mapper_args__ = {'polymorphic_identity': 'assembly_element'}

    assembly_id = db.Column(db.Integer)
    element_id = db.Column(db.Integer)
    quantity_type_id = db.Column(db.Integer)
    quantity = db.column(db.Float)
 
 
class Store(BaseJournalingFields):
    __tablename__ = 'store'

    store_rack_id = db.Column(db.Integer)
    quantity_type_id = db.Column(db.Integer)
    arrival_element_count = db.Column(db.Float)
    expense_element_count = db.Column(db.Float)
    assembly_id = db.Column(db.Integer)
 

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
