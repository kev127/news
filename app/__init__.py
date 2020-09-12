from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

#create the app configurations
app.config.from_object(config_options[config_name])

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing flask extensions
bootstrap.init_app(app)

# Registering the blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

return app