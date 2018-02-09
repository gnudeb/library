from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from .urls import urlpatterns

app_instance = Flask(__name__)
app_instance.config.from_object(Config)
db_instance = SQLAlchemy(app_instance)

for url, view in urlpatterns.items():
    app_instance.add_url_rule(url, view_func=view)
