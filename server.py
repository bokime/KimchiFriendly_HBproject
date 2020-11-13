"""Server for Kimchi Friendly app."""
import os
from flask import Flask, render_template, redirect, request, flash, session, url_for, jsonify
from model import connect_to_db
from forms import Registration, Login, UpdateAccount, NewShare, ZipSearch
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
# from werkzeug.security import generate_password_hash, check_password_hash
# from flaskext.mysql import MySQL

from jinja2 import StrictUndefined

from model import db, User, Share, Review, connect_to_db
import crud


app = Flask(__name__)

app.secret_key = '4e5f639c46265c31'
# app.config["SECRET_KEY"] = os.getenv("appkey")
app.jinja_env.undefined = StrictUndefined
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    """login manager to check current user"""
    return User.query.get(int(user_id))


@app.route('/')
@app.route('/home')
def home():
    """ Home page showing posted jar shares """


    return render_template('home.html', title='Welcome')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """register new user"""

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = Registration()

    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(nickname=form.nickname.data, email=form.email.data, password=pw_hash, zipcode=form.zipcode.data)

        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {form.nickname.data}! Please sign in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)  


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ let user login"""
    
    if current_user.is_authenticated:
        # flash(f"Let's make and share some Kimchi { current_user.nickname }!", "success")
        return redirect(url_for('home'))

    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password", "danger")

    return render_template('login.html', title='Login', form=form) 


@app.route('/logout')
def logout():
    logout_user()
    flash("See you next time", "warning")
    return redirect(url_for('home'))   


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    """ update user profile """

    form = UpdateAccount()
    
    if form.validate_on_submit():
        current_user.nickname = form.nickname.data
        current_user.zipcode = form.zipcode.data

        db.session.commit()

        flash('Profile has been updated!', 'success')
        return redirect(url_for('account'))

    elif request.method == 'GET':
        form.nickname.data = current_user.nickname
        form.zipcode.data = current_user.zipcode

    return render_template('account.html', title='Account', form=form)


######################################## ALL SHARE JARS(potential /home)
@app.route('/share_jars')
def share_jars():
    """ Home page showing posted jar shares """
    shares = crud.get_shares()
    form = ZipSearch()

    return render_template('share_jars.html', shares=shares, form=form, title='Welcome')    


######################################## CREATING NEW JAR SHARE
@app.route('/share_jars/new', methods=['GET', 'POST'])
@login_required
def new_share():
    """ create new kimchi jar share """

    form = NewShare()

    if form.validate_on_submit():
        new_share = Share(share_name=form.share_name.data, made_date=form.made_date.data, description=form.description.data, jar_status=form.jar_status.data)

        db.session.add(new_share)
        db.session.commit()

        flash('Yay! Your new share has been posted!', 'success')
        return redirect(url_for('share_jars'))

    return render_template('new_share.html', title='New Jar Share', form=form, legend='New Share')


@app.route('/share_jars/<int:share_id>')
@login_required
def share(share_id):
    share = Share.query.get_or_404(share_id)
    return render_template('share.html', title=share.share_name, share=share)


@app.route('/share_jars/<string:zipcode>')
@login_required
def share_zipcode(zipcode): 
    """ show Kimchi shares in the user's input zipcode """

    form=ZipSearch()
    
    return render_template('share_jars.html')


@app.route('/user/<string:nickname>')
@login_required
def user_shares(nickname):
    """ show the user's kimchi share history """
    user = User.query.filter_by(nickname=nickname).first_or_404()
    shares = crud.get_shares_by_nickname(nickname)
    return render_template('user_shares.html', shares=shares, user=user)    


# @app.route('/share_jars/<int:share_id>/update', methods=['GET', 'POST'])
# @login_required
# def update_share(share_id):
#     return render_template('new_share.html', title='Update Jar Share', form=form, legend='Update Share')











# @app.route('/', methods=['POST'])
# def index():
#     search = Zipcode_Search()

#     if request.method == 'POST':
#         return search_results(search)
#     return render_template('jar_shares.html', form=search)

# get_shares_by_zipcode(zipcode)
# @app.route('/share_jars/<zipcode>', methods=['POST'])
# def search_results(search):

#     form=Zipcode_Search()

#     results = []
#     search_string = search.data['search']

#     if search_string == '':
#         shares_zipcode = db.session.query(Share.user_id.zipcode)
#         results = shares_zipcode.all()
#     if not results:
#         flash('No results found!')
#         return redirect('/')
#     else:
#         # display results
#         return render_template('jar_shares.html', results=results)      



################################ test:displays all users and all shares 

# @app.route('/all_users')
# def all_users():
#     """View all users."""

#     users = crud.get_users()

#     return render_template('all_users.html', users=users, title='All Users')


# @app.route('/users', methods=['POST'])
# def register_user():
#     """Create a new user"""

#     email = request.form.get('email')
#     password = request.form.get('password')
#     nickname = request.form.get('nickname')
#     zipcode = request.form.get('zipcode')

#     user = crud.get_user_by_email(email)

#     if user:
#         flash('Cannot create an account with that email. Try again.')
#     else:
#         crud.create_user(email, password, nickname, zipcode)
#         flash('Account created! Please log in.')

#     return redirect('/')    


# @app.route('/shares')
# def all_shares():
#     """ view all shares """

#     shares = crud.get_shares()

#     return render_template('all_shares.html', shares=shares)


# @app.route('/shares/<share_id>')
# def show_share(share_id):
#     """Show details on a particular jar share."""

#     user = crud.get_share_by_id(share_id)

#     return render_template('share_details.html', share=share)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     """ user login"""
#     form = Login()

#     if form.validate_on_submit():
#         user = User.query
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')

#     return render_template('login.html', title='Login', form=form) 
    

#######################################################

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)