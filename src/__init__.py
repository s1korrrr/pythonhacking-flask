import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('src.default_settings')
if 'LOCAL_SETTINGS' in os.environ:
    app.config.from_envvar('LOCAL_SETTINGS')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)


import src.views
