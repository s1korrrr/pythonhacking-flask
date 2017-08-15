import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('src.default_settings')
if 'LOCAL_SETTINGS' in os.environ:
    app.config.from_envvar('LOCAL_SETTINGS')

db = SQLAlchemy(app)

import src.views
