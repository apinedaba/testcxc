# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Agency(db.Model):
    __tablename__ = 'agency'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True,)

class Profession(db.Model):
    __tablename__ = 'profession'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True,)

class Ethnicity(db.Model):
    __tablename__ = 'ethnicity'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True,)

class Gender(db.Model):
    __tablename__ = 'gender'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True,)

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    agency_id = db.Column(db.Integer, db.ForeignKey('agency.id'))
    profession_id = db.Column(db.Integer, db.ForeignKey('profession.id'))
    ethnicity_id = db.Column(db.Integer, db.ForeignKey('ethnicity.id'))
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'))
    md5_hash = db.Column(db.String(32), unique=True, nullable=False)
