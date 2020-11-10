"""Server for Kimchi Friendly app."""

from flask import Flask, render_template, redirect, request, flash, session, url_for, jsonify
from model import connect_to_db
from forms import Registration, Login
from jinja2 import StrictUndefined

import crud

app = Flask(__name__)
app.secret_key = '4e5f639c46265c31'
app.jinja_env.undefined = StrictUndefined


@app.route('/')
@app.route('/home')
def home():
    """ view homepage """
    return render_template('home.html', title='Welcome')    


@app.route('/register', methods=['GET', 'POST'])
def register():
    """register new user"""

    form = Registration()

    if form.validate_on_submit():
        flash(f'Account created for {form.nickname.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)  


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ user login"""
    form = Login()

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title='Login', form=form) 


# @app.route('/profile')
# def profile():

#     return render_template('profile.html')    


@app.route('/jar_shares')
def post_jar_shares():
    """ shows posted jar shares page """
    
    shares= crud.get_shares()

    return render_template('jar_shares.html', shares=shares, title='Jar Shares') 



################################ test:displays all users and all shares 

@app.route('/all_users')
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template('all_users.html', users=users, title='All Users')


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
    

#######################################################

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)