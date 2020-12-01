""" Creat Tables for DB Kimchies """

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, foreign
from datetime import datetime, date
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """ A User Table """

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nickname = db.Column(db.String(20), unique=True, nullable=False,)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    zipcode = db.Column(db.String, nullable=False)
    intro = db.Column(db.String, nullable=True)
    phone_number = db.Column(db.String, nullable=True)

    share = db.relationship('Share', backref='users', lazy=True) 
    
    """ Override the default properties of get_id() """
    def get_id(self):
        return (self.user_id)
        
    def __repr__(self):
        return f"""<User user_id={self.user_id} nickname={self.nickname} 
                email={self.email} zipcode={self.zipcode}>"""


class Share(db.Model):
    """ A Jar Sahre Table """

    __tablename__ = 'shares'

    share_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    share_name = db.Column(db.String(120), nullable=False)
    made_date = db.Column(db.Date, nullable=False) #'mm-dd-yy'
    description = db.Column(db.String, nullable=True)
    jar_status = db.Column(db.String(20), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    
    user = db.relationship('User', backref='shares', lazy=True)

    def __repr__(self):
        return f"""<Share share_id={self.share_id} share_name={self.share_name} made_date={self.made_date} jar_status={self.jar_status}>"""


class Review(db.Model):
    """ A Review Table """

    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    review_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False) #'mm-dd-yy'
    comment = db.Column(db.String, nullable=True)
    reviewer_id = db.Column(db.Integer, nullable=False)

    maker_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    user = db.relationship('User', backref='reviews')

    def __repr__(self):
        return f'<Review review_id={self.review_id} reviewer_id={self.reviewer_id} maker_id={self.maker_id}>'        


### Connect db to app -> server.py ###
def connect_to_db(app, db_uri='postgresql:///kimchies', echo=True):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = echo
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app, echo=False)
    # db.create_all()