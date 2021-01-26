import os
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate
from sqlalchemy import Column, String, Integer, Date, DateTime
from sqlalchemy import Boolean, ForeignKey

db = SQLAlchemy()


def setup_db(app):  # , database_path=database_path):
    '''binds a flask application and a SQLAlchemy service
    '''
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    with app.app_context():
        if app.config['DB_NAME'] == 'corona_test':
            db.drop_all()
        db.create_all()


class Restaurant(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    street = db.Column(db.String(50))
    owner = db.Column(db.String(150))
    email = db.Column(db.String(150))
    amount_of_tables = db.Column(db.Integer(), nullable=True)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    last_modified_date = db.Column(db.DateTime, default=func.now())

    def json_repr(self):
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country,
            'city': self.city,
            'postcode': self.postcode,
            'street': self.street,
            'owner': self.owner,
            'email': self.email,
            'amount_of_tables': self.amount_of_tables,
            'creation_date': self.creation_date,
            'last_modified_date': self.last_modified_date
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        self.last_modified_date = func.now()
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.json_repr())


class Table(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    restaurant_id = db.Column(db.Integer(), db.ForeignKey(
        'restaurant.id'), nullable=False)
    # is_soft_deleted = db.Column(Boolean() default=False, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    last_modified_date = db.Column(db.DateTime, default=func.now())

    def json_repr(self):
        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id,
            # 'is_soft_deleted': self.is_soft_deleted,
            'creation_date': self.creation_date,
            'last_modified_date': self.last_modified_date
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.last_modified_date = func.now()
        db.session.commit()

    def soft_delete(self):
        self.last_modified_date = func.now()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.json_repr())


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    sick = db.Column(db.Boolean(), default=False, nullable=False)
    sick_since = db.Column(db.Date())
    creation_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    last_modified_date = db.Column(db.DateTime, default=func.now())

    def json_repr(self):
        return {
            'id': self.id,
            'name': self.name,
            'street': self.street,
            'city': self.city,
            'postcode': self.postcode,
            'country': self.country,
            'email': self.email,
            'sick': self.sick,
            'sick_since': self.sick_since,
            'creation_date': self.creation_date,
            'last_modified_date': self.last_modified_date
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.last_modified_date = func.now()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.json_repr())


class Visit(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    restaurant_id = db.Column(db.Integer(), db.ForeignKey(
        'restaurant.id'), nullable=False)
    table_id = db.Column(db.Integer(), db.ForeignKey(
        'table.id'), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    visit_start_dt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    visit_end_dt = db.Column(db.DateTime())

    def json_repr(self):
        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id,
            'table_id': self.table_id,
            'user_id': self.user_id,
            'visit_start_dt': self.visit_start_dt,
            'visit_end_dt': self.visit_end_dt,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.json_repr())
