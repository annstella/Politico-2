from flask import Flask
from .config import DevConfig
from app.api.V1 import Version1

# Initializing application
def create_app(config_name):

    app = Flask(__name__)

app=Flask(__name__)
app.register_blueprint(Version1)

# Setting up configuration
app.config.from_object(config_options[config_name])

from app import views