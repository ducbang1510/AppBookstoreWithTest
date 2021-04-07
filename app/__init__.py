from flask import Flask, render_template
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
admin = Admin(name="Quản lý nhà sách", template_mode="bootstrap4")  # base_template="layout.html"
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config)
    initialize_extensions(app)
    register_blueprints(app)

    @app.route("/")
    def index():
        return render_template('index.html')

    return app


def initialize_extensions(app):
    db.init_app(app=app)
    admin.init_app(app=app)
    login_manager.init_app(app=app)
    bcrypt.init_app(app=app)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()


def register_blueprints(app):
    from app.users import users_blueprint

    app.register_blueprint(users_blueprint)