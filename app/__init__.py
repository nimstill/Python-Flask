from flask import Flask
from flase.ext.sqlalchemy import SQLAchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAchemy(app)

from app import views, models


import os
from flask.ext.login import LoginManger
from flask.ext.openid import OpenID
from config import basedir 

lm = LoginManger()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))


