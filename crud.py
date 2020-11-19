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
### test example: create_user('lena', 'lena@test.com', 'password', '12345', 'I like kimchi!')    


def create_share(share_name, made_date, description, jar_status, user_id):
    """ create a new jar share """

    share = Share(
                    share_name=share_name, made_date=made_date, description=description, jar_status=jar_status,
                    user_id=user_id
                    )

    db.session.add(share)
    db.session.commit()

    return share
### test example: create_share('red cabbage kimchi', '05-23-19', 'very spicy and tangy! so good!', 'sold', '2')  

# def create_review(rating, review_date, comment, reviewer_id, share_id, reviewee_id):
    
#     """ create a new review """

#     review = Review(
#                     rating=rating,
#                     review_date=review_date,
#                     comment=comment,
#                     reviewer_id=reviewer_id,
#                     share_id=share_id,
#                     reviewee_id=reviewee_id
#                     )

#     db.session.add(review)
#     db.session.commit()

#     return review


def create_review(rating, review_date, comment):
    
    """ create a new review """

    review = Review(
                    rating=rating,
                    review_date=review_date,
                    comment=comment
                    )

    db.session.add(review)
    db.session.commit()

    return review




def load_user(user_id):
    """ return a user by primary key """

    return User.query.get(int(user_id))


#####
def get_shares():
    """ return all jar shares """

    return Share.query.all()


def get_share_by_id(share_id):
    """ return a share by primary key """

    return Share.query.get(share_id)    


#####
def get_shares_by_zipcode(zipcode):
    """ query user zipcode from User obj for Share (Left Join) """ 

    return db.session.query(Share).join(User).filter(User.zipcode == zipcode).all() 


#####
def get_shares_by_nickname(nickname):
    """ query user nickname from User obj for Share (Left Join) """ 

    return db.session.query(Share).join(User).filter(User.nickname == nickname).all()     




if __name__ == '__main__':

    from server import app

    connect_to_db(app, echo=False)
