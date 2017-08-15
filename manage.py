from flask_script import Manager, prompt_bool

from src.main import app

manager = Manager(app)


if __name__ == '__main__':
    manager.run()
