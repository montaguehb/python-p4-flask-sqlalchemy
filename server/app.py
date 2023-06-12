#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

migrate = Migrate(app, db)

db.init_app(app)

class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    pets = db.relationship('Pet', backref='owner')

    def __repr__(self):
        return f'<Pet Owner {self.name}>'

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    def __repr__(self):
        return f'<Pet {self.name}, {self.species}>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
