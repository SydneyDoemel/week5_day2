from flask import Flask
from config import Config
from .saved_pokes.routes import saved_pokes
from .search.routes import search
app = Flask(__name__)
app.register_blueprint(saved_pokes)
app.register_blueprint(search)
app.config.from_object(Config)
from . import routes