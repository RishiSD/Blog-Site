from flask import Flask
from flask_simplemde import SimpleMDE
from flask_mongoengine import MongoEngine
from flaskext.markdown import Markdown
from flask_login import LoginManager
from FlaskBlogApp.config import Config

smde = SimpleMDE()
db = MongoEngine()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    smde.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    Markdown(app)

    from FlaskBlogApp.posts.routes import posts
    from FlaskBlogApp.user.routes import user
    from FlaskBlogApp.navigation.routes import navigation
    from FlaskBlogApp.utils import (
        unauthorized_access,
        page_not_found,
        user_loader
    )
    app.register_blueprint(posts)
    app.register_blueprint(user)
    app.register_blueprint(navigation)
    app.register_error_handler(401, unauthorized_access)
    app.register_error_handler(404, page_not_found)

    return app
