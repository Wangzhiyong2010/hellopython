from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask("hellopython")
# 在扩展类实例化前加载配置

app.config.from_pyfile('config.py')


db = SQLAlchemy(app)



login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    from hellopython.models import User
    user = User.query.get(int(user_id))
    return user

login_manager.login_view = 'login'

@app.context_processor
def inject_user():
    from hellopython.models import User
    user = User.query.first()
    return dict(user = user)


from hellopython import commands, views
