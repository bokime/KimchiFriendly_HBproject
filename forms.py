from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from model import User, Share, Review



class Registration(FlaskForm):
    """ register new user """
    
    nickname = StringField('Nickname',
                            validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                        validators=[DataRequired(), EqualTo('password')])
    zipcode = StringField('Zipcode', validators=[DataRequired(), Length(min=3, max=10)])                                    
    submit = SubmitField('Sign Up')

    def check_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Sorry, this email is taken.')

    def check_nickname(self, nickname):
        user = User.query.filter_by(nickname=nickname.data).first()
        if user:
            raise ValidationError('Sorry, this nickname is taken.')


class Login(FlaskForm):
    """ login form """

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')  


class UpdateAccount(FlaskForm):
    """ update account form """

    nickname = StringField('Nickname', validators=[DataRequired(), Length(min=2, max=20)])

    password = StringField('Password')
    zipcode = StringField('Zipcode')
    submit = SubmitField('Update')

    def validate_nickname(self, nickname):
        if nickname.data != current_user.nickname:
            user = User.query.filter_by(nickname=nickname.data).first()
            if user:
                raise ValidationError('Sorry, this nickname exist.')


class NewShare(FlaskForm):
    """ new jar share form """

    share_name = StringField('Title', validators=[DataRequired()])
    made_date = DateField('When did you make?', format='%m-%d-%y')
    description = TextAreaField('About This Kimchi: ', validators=[DataRequired()])
    jar_status = StringField('Status')
    submit = SubmitField('New Share')


