import os

from app import create_app

config_name = os.getenv('FAS_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
