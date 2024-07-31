from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from .config import *

from flask_login import LoginManager

csrf = CSRFProtect()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')


    from app.models import User, Event

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    return app

    