# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('u_name',validators=[DataRequired(),Length(max = 10)])
    password = PasswordField('pass',validators=[DataRequired()])
    confirm_password = PasswordField('confirm_pass',validators=[DataRequired(),EqualTo(password)])
    submit = SubmitField('signUp')
