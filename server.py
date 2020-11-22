"""Server for Kimchi Friendly app."""
import os
import crud

from flask import Flask, render_template, redirect, request, flash, session, url_for
from model import connect_to_db
from forms import Registration, Login, UpdateAccount, NewShare, Review
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

from jinja2 import StrictUndefined
from model import db, User, Share, Review, connect_to_db
# from twilio.rest import Client


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

    page = request.args.get('page', 1, type=int)
    shares = Share.query.order_by(Share.made_date.desc()).paginate(page=page, per_page=4) 
    # shares = crud.get_shares()
    return render_template('home.html', shares=shares, title='Welcome')



@app.route('/register', methods=['GET', 'POST'])
def register():
    """register new user"""

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = Registration()

    if form.validate_on_submit():

        pw_hash = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(nickname=form.nickname.data,
                    email=form.email.data,
                    phone_number=form.phone_number.data,
                    password=pw_hash,
                    zipcode=form.zipcode.data,
                    intro=form.intro.data)

        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {form.nickname.data}! Please sign in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)  



@app.route('/login', methods=['GET', 'POST'])
def login():
    """ user login verification """
    
    if current_user.is_authenticated:
        flash(f"Let's make and share some Kimchi Jars, { current_user.nickname }!", "success")
        return redirect(url_for('home'))

    form = Login()
    if form.validate_on_submit():
        # get user by email
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            
            session['user_id']= user.user_id
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password", "danger")

    return render_template('login.html', title='Login', form=form) 



@app.route('/logout')
def logout():
    """ user logout """

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
        current_user.phone_number = form.phone_number.data
        current_user.zipcode = form.zipcode.data
        current_user.intro = form.intro.data

        db.session.commit()

        flash('Profile has been updated!', 'success')
        return redirect(url_for('account'))

    elif request.method == 'GET':
        form.nickname.data = current_user.nickname
        form.phone_number.data = current_user.phone_number
        form.zipcode.data = current_user.zipcode
        form.intro.data = current_user.intro

    return render_template('account.html', title='Account', form=form)



@app.route('/home', methods=['POST'])
@login_required
def share_zipcode(): 
    """ show Kimchi shares in the user's input zipcode """

    zipcode = request.form.get('zipcode')
    shares = crud.get_shares_by_zipcode(zipcode)

    return render_template('share_zipcode.html', shares=shares, zipcode=zipcode)



@app.route('/home/new', methods=['GET', 'POST'])
@login_required
def new_share():
    """ create new kimchi jar share """

    form = NewShare()

    if request.method == "POST":

        new_share = Share(share_name=form.share_name.data,
                        made_date=form.made_date.data,
                        description=form.description.data, 
                        jar_status=form.jar_status.data, 
                        user_id=session['user_id'])

        db.session.add(new_share)
        db.session.commit()

        flash('Yay! Your new share has been posted!', 'success')
        return redirect(url_for('home'))

    return render_template('new_share.html', title='New Jar Share', form=form, legend='New Share')



@app.route('/home/<share_id>')
def share(share_id):
    """ show the detail of each Kimchi Jar Share """

    share = Share.query.get_or_404(share_id)

    return render_template('share.html', title=share.share_name, share=share)



@app.route('/home/<share_id>/update', methods=['GET', 'POST'])
@login_required
def update_share(share_id):
    """ update user's share posting """

    update_share = Share.query.get_or_404(share_id)

    if update_share.user_id != current_user.user_id:
        flash('Are you sure this is your Kimchi share?', 'danger')
        return redirect(url_for('home'))
    
    form = NewShare()

    if request.method == "POST":
        update_share.share_name = form.share_name.data
        update_share.made_date = form.made_date.data
        update_share.jar_status = form.jar_status.data
        update_share.description = form.description.data
    
        db.session.commit()

        flash('Your new jar share has been updated!', 'success')
        return redirect(url_for('home', share_id=update_share.share_id))
    
    elif request.method == "GET":
        form.share_name.data = update_share.share_name
        form.made_date.data = update_share.made_date
        form.jar_status.data = update_share.jar_status
        form.description.data = update_share.description
    
    return render_template('new_share.html', title='Update Jar Share', form=form, legend='Update Jar Share')



@app.route('/home/<share_id>/delete', methods=['POST'])
@login_required
def delete_share(share_id):
    """ delete user's share posting """

    delete_share = Share.query.get(share_id)

    if delete_share.user_id != current_user.user_id:
        flash('Watch out! This is not your Kimchi share.', 'danger')
        return redirect(url_for('home'))

    else:    
        db.session.delete(delete_share)
        db.session.commit()
        
        flash('Your Kimchi Share Posting has been deleted.', 'sucess')
        return redirect(url_for('home'))



@app.route('/user/<nickname>')
@login_required
def user_shares(nickname):
    """ show the user's kimchi share history """

    user = User.query.filter_by(nickname=nickname).first_or_404()
    # page = request.args.get('page', 1, type=int)
    # get_review = crud.get_reviews_by_user_id(user_id=user.user_id)
    shares = crud.get_shares_by_nickname(nickname)

    return render_template('user_profile.html', shares=shares, user=user)   


###### reviwer's nickname has to be passed
## creating review    
@app.route('/user/<nickname>', methods=['POST'])
@login_required
def user_review(nickname): 
    """ add new Kimchi maker review """

    if request.method == 'POST':

        rating = request.form.get('rating')
        review_date = request.form.get('review_date')
        comment = request.form.get('review_comment')
        maker_id = request.form.get('maker_id')
        reviewer_id = session['user_id']

        make_review = crud.create_review(rating, review_date,
                                    comment, reviewer_id, maker_id)
        
        db.session.add(make_review)
        db.session.commit()

        flash('Your review has been submitted!', 'success')
    return redirect(f'/user/{nickname}')


###### redirect(/user/<nickname>)
## Deleting review
@app.route('/user/<review_id>/delete', methods=['POST'])
@login_required
def delete_review(review_id):
    """ delete user's review """
    
    delete_review = Review.query.get(review_id)

    db.session.delete(delete_review)
    db.session.commit()
    
    flash('Your review has been deleted.', 'sucess')
    return redirect('/')




if __name__ == '__main__':
    connect_to_db(app)
    app.run(port=5000, host='0.0.0.0', debug=True)





# ## Deleting review
# @app.route('/user/<review_id>/delete', methods=['POST'])
# @login_required
# def delete_review(review_id):
#     """ delete user's review """
    
#     delete_review = Review.query.get(review_id)

#     db.session.delete(delete_review)
#     db.session.commit()
    
#     flash('Your review has been deleted.', 'sucess')
#     return redirect('/')