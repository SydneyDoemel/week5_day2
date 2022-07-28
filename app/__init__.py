from flask import Flask
from config import Config
from .saved_pokes.routes import saved_pokes
from .search.routes import search
from .auth.routes import auth
app = Flask(__name__)
app.register_blueprint(saved_pokes)
app.register_blueprint(search)
app.register_blueprint(auth)
app.config.from_object(Config)

from .models import db 
from flask_migrate import Migrate

db.init_app(app)
migrate = Migrate(app,db)

from . import routes
from . import models