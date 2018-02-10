#!/usr/bin/env python3
from flask_script import Manager
from app.app import app_instance

manager = Manager(app_instance)

if __name__ == '__main__':
    manager.run()
