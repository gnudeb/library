import json
import os.path

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SECRETS_FILEPATH = os.path.join(BASE_DIR, 'secrets.json')

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

with open(SECRETS_FILEPATH, 'r') as secrets_file:
    secrets = json.load(secrets_file)

MAIL_SERVER = 'smtp.sendgrid.net'
MAIL_DEFAULT_SENDER = 'library'
MAIL_USERNAME = secrets['MAIL_USERNAME']
MAIL_PASSWORD = secrets['MAIL_PASSWORD']
