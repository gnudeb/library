from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

app_instance = Flask(__name__)
app_instance.config.from_object('app.config')
db_instance = SQLAlchemy(app_instance)
mail_instance = Mail(app_instance)

from .urls import urlpatterns
for url, view in urlpatterns.items():
    app_instance.add_url_rule(url, view_func=view)
