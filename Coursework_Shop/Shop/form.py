from flask_wtf import FlaskForm
from wtfforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class sign_up_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Regexp('^.{3,15}$', message='Your password needs to be between 3 and 15 characters long')])
    passwordVerify = PasswordField('Confirm Your Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    def valid_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose another username.')
    def valid_email(self, email):
        mail = User.query.filter_by(email=email.data).first()
        if mail:
            raise ValidationError('This email is already being used please try another email.')

class login_form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
