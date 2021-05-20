from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import (DataRequired, Email,
                                Length, EqualTo)
from pasman.models import User
from wtforms.fields.html5 import IntegerRangeField


class RegistrationForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(),
                                       Length(min=2, max=20,
                                              message='Username should be between 2 and 20 letters.')])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password',
                                                         message="Both the password must be equal.")])
    submit = SubmitField('Submit')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                "Email is already taken. Please choose another one")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                "Username is already taken. Please choose another one")


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Register')


class AddPostForm(FlaskForm):
    app = StringField("Application")
    username = StringField('Username')
    email = StringField('Email')
    password = PasswordField("Password")
    password_len = IntegerRangeField("Password_len", default=8)
    generate = BooleanField('Generate')
    view = BooleanField('View Password')
    submit = SubmitField('Save')
