from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import datetime

db = SQLAlchemy()

class Restaurant(db.Model):
    id = Column(Integer(), primary_key=True)
    name = Column(String_(100), nullable=False)
    country = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    postcode = Column(String(10), nullable=False)
    street = Column(String(50))
    owner = Column(String(150))
    email = Column(String(150))
    amount_of_tables = Column(Integer(), nullable=True)
    creation_date = Column(DateTime, default=datetime.datetime.utcnow)
    last_modified_date = Column(DateTime, default=func.now())

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
        self.last_modified_date=func.now()
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.json_repr())


class Table(db.Model):
    id = Column(Integer(), primary_key=True)
    restaurant_id = Column(Integer(), c)
    is_soft_deleted = Column(Boolean() default=False, nullable=False)
    creation_date = Column(DateTime, default=datetime.datetime.utcnow)
    last_modified_date = Column(DateTime, default=func.now())

    def json_repr(self):
        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id,
            'is_soft_deleted': self.is_soft_deleted,
            'creation_date': self.creation_date,
            'last_modified_date': self.last_modified_date
            }

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        self.last_modified_date=func.now()
        db.session.commit()
    
    def soft_delete(self):
        self.is_soft_deleted = True
        self.last_modified_date=func.now()
        db.session.commit()

    def hard_delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.json_repr())


class User(db.Model):
    id = Column(Integer(), primary_key=True)
    name = Column(String_(100), nullable=False)
    street = Column(String(50), nullable=False)
    city = Column(String(100), nullable=False)
    postcode = Column(String(10), nullable=False)
    country = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    sick = Column(Boolean(), default=False, nullable=False)
    sick_since = Column(Date())
    creation_date = Column(DateTime, default=datetime.datetime.utcnow)
    last_modified_date = Column(DateTime, default=func.now())

    def json_repr(self):
        return {
            'id': self.id,
            'name': self.name,
            'street': self.street,
            'city': self.city,
            'postcode': self.postcode,
            'country:' self.country,
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
        self.last_modified_date=func.now()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.json_repr())


class Visit(db.Model):
    id = Column(Integer(), primary_key=True)
    restaurant_id = Column(Integer(), ForeignKey('restaurant.id'), nullable=False)
    table_id = Column(Integer(), ForeignKey('table.id'), nullable=False)
    user_id = Column(Integer(), ForeignKey('user.id'), nullable=False)
    visit_start_dt = Column(DateTime, default=datetime.datetime.utcnow)
    visit_end_dt = Column(DateTime()))

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