#!/usr/bin/env python3
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.app import app_instance, db_instance

migrate = Migrate(app_instance, db_instance)
manager = Manager(app_instance)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
