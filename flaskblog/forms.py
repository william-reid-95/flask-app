from xml.dom import ValidationErr
from flask_wtf import FlaskForm
# converts python classes into html forms
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(2,20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        #query db for user of existing name and raise error if username is already in db
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username is already in use.")
    
    def validate_email(self, email):
        #query db for user of existing email and raise error if email is already in db
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email address is already in use.")


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    