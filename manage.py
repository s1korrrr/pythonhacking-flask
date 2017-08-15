from flask_script import Manager, prompt_bool

from src.views import app

manager = Manager(app)


if __name__ == '__main__':
    manager.run()
