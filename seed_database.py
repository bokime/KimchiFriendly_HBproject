""" seed dummy data into the tables """

import os
import json

from random import choice, randint
from datetime import datetime, date, time

import crud
import model
import server

os.system('dropdb kimchies')
os.system('createdb kimchies')

model.connect_to_db(server.app)#, echo=False)

model.db.create_all()


""" seed dummy user data """
with open('data/users.json') as u:
    user_data = json.loads(u.read())


for user in user_data:

    nickname = user['nickname']
    email = user['email']
    password = user['password']
    zipcode = user['zipcode']
    intro = user['intro']

    crud.create_user(nickname, email, password, zipcode, intro)



""" seed dummy jar share data """
with open('data/shares.json') as f:
    share_data = json.loads(f.read())

for share in share_data:

    share_name = share['share_name']
    made_date = datetime.strptime(share['made_date'], '%m-%d-%y')
    description = share['description']
    jar_status = share['jar_status']
    user_id = share['user_id'] 


    crud.create_share(share_name, made_date, description, jar_status, user_id)



""" seed dummy review data """
with open('data/reviews.json') as r:
    review_data = json.loads(r.read())

for review in review_data:

    rating = review['rating']
    review_date = datetime.strptime(review['review_date'], '%m-%d-%y')
    comment = review['comment']
    reviewer_id = review['reviewer_id']
    maker_id = review['maker_id']

    crud.create_review(rating, review_date, comment, reviewer_id, maker_id)
