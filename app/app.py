from flask import Flask
from flask_mail import Mail
from pymongo import MongoClient
from .config import MONGO_HOST, MONGO_PORT

app_instance = Flask(__name__)
app_instance.config.from_object('app.config')

db_client = MongoClient(MONGO_HOST, MONGO_PORT)
db_instance = db_client.db

mail_instance = Mail(app_instance)

from .urls import urlpatterns
for url, view in urlpatterns.items():
    app_instance.add_url_rule(url, view_func=view)
