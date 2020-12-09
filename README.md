# KimchiFriendly

> KimchiFriendly is inspired by the traditional Kimchi sharing culture  in Korea; my grandmother used to make 100 cabbages per batch to share with family and neighbors. Kimchi is not just a healthy and  tasty food, but also a part of creating our warm sharing culture. 

## Tech stack

  - Python
  - Flask (WTForms, LoginManager)
  - Jinja2
  - PostgresSQL
  - SQLAlchemy ORM
  - Javascript(jQuery/AJAX)
  - Bootstrap
  - HTML
  - CSS
  - Twilio API

## Features

  - User's registration, Login, Logout, Edit account.

  ![](https://github.com/bokime/KimchiFriendly_HBproject/blob/master/static/gifs/signin.gif)


  - Zipcode search to find Kimchi makers in the user's area.
  - Send Request Kimchi jars via Twilio API.
  
  ![](https://github.com/bokime/KimchiFriendly_HBproject/blob/master/static/gifs/zipsearch.gif)
  
  
  - Posting new Kimchi jar sharing, update, delete.
  
  ![](https://github.com/bokime/KimchiFriendly_HBproject/blob/master/static/gifs/posting.gif)
  
  
  - Display the history of Kimchi maker's jar postings.
  
  - Leave a review of Kimchi maker, delete. 
  
  ![](https://github.com/bokime/KimchiFriendly_HBproject/blob/master/static/gifs/review.gif)
  
## MVPs

- User registration and login. 
- Update profile.
- Display all Kimchi jar shares and show each user's share history.
- Check each Jar Share details.
- Create/edit/delete new jar shares.
- Search zip code to navigate Kimchi Jar Shares in the user's area.
- Filter Share status( ‘fermenting’, ‘ready to share’, 'shared') 
- Users can request available Kimchi jar share. (Twilio API)
- Leave a review/ delete for jar sharing experience on Maker's profile.

## Database

> Each unique User can create multiple Share and Review in one to many relationships as if we share our Kimchi with family and friends in real life. 

  ![](https://github.com/bokime/KimchiFriendly_HBproject/blob/master/static/img/KimchiFriendly_db.jpeg)


## Installation

- Install PostgreSQL

- Clone KimchiFriendly repo:

```sh
https://github.com/bokime/KimchiFriendly_HBproject.git
```
- Create and activate a virtual environment in the project directory:

```sh
$ virtualenv env
$ source env/bin/active
```

- Install dependencies:

```sh
pip install -r requirements.txt
```

- Save your API keys in a file called "secrets.sh":

```sh
$ source secrets.sh
```

- Set up the database:

```sh
createdb kimchies
python3 model.py
```

- Run the app:

```sh
python3 server.py
```
