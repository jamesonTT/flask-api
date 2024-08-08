from flask import Flask
from server.config import Config
from server.register_blueprints import register_blueprints
app = Flask(__name__)
app.config.from_object(Config)

if __name__ == '__main__':
    register_blueprints(app)
    app.run(host=app.config.get('APP_HOST'), port=app.config.get('APP_PORT'), debug=app.config.get('APP_DEBUG_MODE'))
