from app import create_app
from flask_script import Manager, Server

app = create_app('development')

Manager = Manager(app)
Manager.add_command('server', Server)

if __name__ == '__main__':
    Manager.run()