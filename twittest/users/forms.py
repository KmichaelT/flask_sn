from dataclasses import Field
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from twittest.models import User

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()],render_kw={"placeholder": "Email"})
    password = PasswordField('Password',validators=[DataRequired()],render_kw={"placeholder": "Password"})
    submit= SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()],render_kw={"placeholder": "Email"})
    username=StringField('Username',validators=[DataRequired()],render_kw={"placeholder": "Username"})
    password = PasswordField('Password',validators=[DataRequired(), EqualTo('conf_password', message='Password must match!')],render_kw={"placeholder": "Password"})
    conf_password = PasswordField('Confirm Password',validators=[DataRequired()],render_kw={"placeholder": "Confirm Password"})
    submit= SubmitField('Register')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError( ' Email already registerd! ')

    def check_username (self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError( ' username already registerd! ')

class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username=StringField('Username',validators=[DataRequired()])
    picture=FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])],render_kw={"placeholder": "Update profile picture"})
    submit= SubmitField('Update')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError( ' email already registerd! ')

    def check_username (self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError( ' username already registerd! ')