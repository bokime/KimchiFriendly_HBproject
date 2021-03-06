""" CRUD(Creat, Read, Update, Delete) Operations to query dababase. """

from model import db, User, Share, Review, connect_to_db


def create_user(nickname, email, password, zipcode, intro):
    """ create and return a new user """

    user = User(
                nickname=nickname,
                email=email,
                password=password,
                zipcode=zipcode,
                intro=intro
                )

    db.session.add(user)
    db.session.commit()

    return user


def create_share(share_name, made_date, description, jar_status, user_id):
    """ create a new jar share """

    share = Share(
                    share_name=share_name, made_date=made_date, description=description, jar_status=jar_status,
                    user_id=user_id
                    )

    db.session.add(share)
    db.session.commit()

    return share


def create_review(rating, review_date, comment, reviewer_id, maker_id):
    """ create a new review """

    review = Review(
                    rating=rating,
                    review_date=review_date,
                    comment=comment,
                    reviewer_id=reviewer_id,
                    maker_id=maker_id
                    )

    db.session.add(review)
    db.session.commit()

    return review


def load_user(user_id):
    """ return a user by primary key """

    return User.query.get(int(user_id))


def get_shares():
    """ return all jar shares """

    return Share.query.all()


def get_shares_by_zipcode(zipcode):
    """ query user zipcode from User obj for Share (Left Join) """ 

    # return db.session.query(Share).join(User).filter(User.zipcode == zipcode).all() 
    # sorting
    return db.session.query(Share).join(User).filter(User.zipcode == zipcode).order_by(Share.made_date.desc()) 

def get_shares_by_user_id(user_id):
    """ query user nickname from User obj for Share (Left Join) """ 

    return db.session.query(Share).join(User).filter(User.user_id == user_id).all()  


if __name__ == '__main__':

    from server import app
    connect_to_db(app, echo=False)