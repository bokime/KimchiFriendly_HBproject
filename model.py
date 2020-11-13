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

    share = db.relationship('Share', backref='users', lazy=True) 
    
    # def get_id(self):
    #     return (self.user_id)
        
    def __repr__(self):
        return f"""<User user_id={self.user_id} nickname={self.nickname} 
                email={self.email} zipcode={self.zipcode}>"""


class Share(db.Model):
    """ A Jar Sahre Table """

    __tablename__ = 'shares'

    share_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    share_name = db.Column(db.String(120), nullable=False)
    made_date = db.Column(db.Date, nullable=False) #'mm-dd-yy'
    description = db.Column(db.String, nullable=False)
    jar_status = db.Column(db.String(20), nullable=False)
    # img = db.Column(db.String(20), nullable=True, default='default.jpg')

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    
    user = db.relationship('User', backref='shares', lazy=True)

    def __repr__(self):
        return f"""<Share share_id={self.share_id} share_name={self.share_name} made_date={self.made_date} jar_status={self.jar_status}>"""



class Review(db.Model):
    """ A Review Table """

    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    review_date = db.Column(db.Date, nullable=False) #'mm-dd-yy'
    comment = db.Column(db.String, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'), nullable=False)
    share_id = db.Column(db.Integer, db.ForeignKey('shares.share_id'), nullable=False)

    user = db.relationship('User', backref='reviews')
    # recipe = db.relationship('Recipe', backref='reviews')
    share = db.relationship('Share', backref='reviews')

    def __repr__(self):
        return f'<Review review_id={self.review_id} review_date={self.review_date} score={self.score}>'        



# class Recipe(db.Model):
#     """ A Recipe Table """

#     __tablename__ = 'recipes'

#     recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     recipe_title = db.Column(db.String(60), nullable=False)
#     recipe_date = db.Column(db.Date, nullable=False) #'mm-dd-yy'
#     description = db.Column(db.String, nullable=False)

#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

#     user = db.relationship('User', backref='recipes')

#     def __repr__(self):
#         return f"""<Recipe recipe_id={self.recipe_id} title={self.recipe_title} description={self.description}>"""



# class Photo(db.Model):
#     """ A Photo Table """

#     __tablename__ = 'photos'

#     photo_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     post_date = db.Column(db.DateTime, nullable=False)
#     # img = db.Column(db.String(20), nullable=False, default='default.jpg')

#     recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'), nullable=False)
#     share_id = db.Column(db.Integer, db.ForeignKey('shares.share_id'), nullable=False)

#     recipe = db.relationship('Recipe', foreign_keys=[recipe_id])
#     share = db.relationship('Share', foreign_keys=[share_id])

#     def __repr__(self):
#         return f'<Photo photo_id={self.photo_id} post_date={self.post_date}>'



######### Connect db to app -> server.py #########

def connect_to_db(app, db_uri='postgresql:///kimchies', echo=True):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = echo
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every query it executes.

    connect_to_db(app, echo=False)
    # db.create_all()

    # new_user = User(nickname='testkim', email='bk@gmail.com', password='password', zipcode=12345)
    # db.session.add(new_user)
    # db.session.commit()
    
    # new_share = Share(share_name='radish', made_date='05-23-20', jar_status='fermenting', user_id='1')
    # db.session.add(new_share)
    # db.session.commit()

    # new_review = Review(score=8, review_date='03-28-20', user_id='1', share_id='1') 
    # db.session.add(new_review)
    # db.session.commit()
    
    # new_recipe = Recipe(recipe_title='kimchi01', recipe_date='02-23-19', description='this is the best summer kimchi. easy to make')
    # db.session.add(new_recipe)
    # db.session.commit()
