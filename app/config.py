import json
import os.path

SQLALCHEMY_DATABASE_URI = "postgresql://localhost/library"
SQLALCHEMY_TRACK_MODIFICATIONS = False
MAIL_SERVER = 'smtp.sendgrid.net'
MAIL_DEFAULT_SENDER = 'library'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SECRETS_FILEPATH = os.path.join(BASE_DIR, 'secrets.json')

with open(SECRETS_FILEPATH, 'r') as secrets_file:
    secrets = json.load(secrets_file)
MAIL_USERNAME = secrets['MAIL_USERNAME']
MAIL_PASSWORD = secrets['MAIL_PASSWORD']
