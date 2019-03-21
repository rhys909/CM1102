from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from Shop.models import User

class sign_up_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired('Please enter your username'), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Regexp('^.{6,15}$', message='Your password needs to be between 6 and 15 characters long')])
    passwordVerify = PasswordField('Confirm Your Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
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

class checkout_form(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired('Please enter your first name.'), Length(min=3, max=15)])
    last_name = StringField('Last Name', validators=[DataRequired('Please enter your last name.'), Length(min=3, max=15)])
    address_line_1 = StringField('Address Line 1', validators=[DataRequired('Please enter your address'), Length(min=5, max=30)])
    address_line_2 = StringField('Address Line 2')
    address_line_3 = StringField('Address Line 3')
    county = StringField('County', validators=[DataRequired('Please enter your county!'), Length(min=3, max=26)])
    postcode = StringField('Postcode', validators=[DataRequired('Please enter your postcode!', length(min=5, max=7)])
