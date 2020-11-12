""" CRUD(Creat, Read, Update, Delete) Operations to query dababase. """

from model import db, User, Share, Review, connect_to_db


def create_user(nickname, email, password, zipcode, intro):
    """ create and return a new user """

    user = User(nickname=nickname, email=email, password=password, zipcode=zipcode, intro=intro)

    db.session.add(user)
    db.session.commit()

    return user
### test example: create_user('lena', 'lena@test.com', 'password', '12345', 'I like kimchi!')    

def get_users():
    """Return all users."""
    
    return User.query.all()    


def load_user(user_id):
    """ return a user by primary key """

    return User.query.get(int(user_id))


def get_user_by_email(email):
    """ return a user by email """

    return User.query.filter(User.email == email).first()


def create_share(share_name, made_date, description, jar_status, user_id):
    """ create a new jar share """

    share = Share(share_name=share_name, made_date=made_date, description=description, jar_status=jar_status, user_id=user_id)

    db.session.add(share)
    db.session.commit()

    return share
### test example: create_share('red cabbage kimchi', '05-23-19', 'very spicy and tangy! so good!', 'sold', '2')    


def get_shares():
    """ return all jar shares """

    return Share.query.all()

def get_share_by_id(share_id):
    """ return a share by primary key """

    return Share.query.get(share_id)

def get_share_by_share_name(share_name):
    """ return a share by primary key """

    return Share.query.get(share_name)    


def get_shares_by_zipcode(zipcode):
    """ query user zipcode from User obj for Share (Left Join) """ 

    return db.session.query(Share).join(User).filter(User.zipcode == zipcode).all() 


# def create_recipe(recipe_title, recipe_date, description, photo):
#     """ create and return a new recipe """

#     recipe = Recipe(recipe_title=recipe_title, recipe_date=recipe_date, description=description, photo=photo)

#     db.session.add(recipe)
#     db.session.commit()

#     return recipe


# def create_review(user, share, score):
#     """ create and return a new review """

#     review = Review(user=user, share=share, score=score)

#     db.session.add(review)
#     db.session.commit()

#     return review


# def create_photo(post_date):
#     """ create and return a new photo """

#     photo = Photo(post_date=post_date)

#     db.session.add(photo)
#     db.session.commit()

#     return photo


if __name__ == '__main__':

    from server import app

    connect_to_db(app, echo=False)
