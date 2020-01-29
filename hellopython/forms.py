
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, Form
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
    username = StringField('用户名', validators = [DataRequired(), Length(1, 20)])
    password = StringField('密码', validators = [DataRequired(), Length(1, 20)])
    login = SubmitField('登录')
