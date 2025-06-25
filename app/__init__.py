from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models import db, User
from config import Config
from flask_migrate import Migrate

# Flask extensions
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Redirect to login if not logged in
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    # Configuration
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from .auth import auth as auth_blueprint
    from .routes import main as main_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    migrate = Migrate(app, db)

    return app

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))