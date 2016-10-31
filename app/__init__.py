from flask import Flask
from flase.ext.sqlalchemy import SQLAchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAchemy(app)

from app import views, models


