# Import Required Modules

from pathlib import Path

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

from flask_migrate import Migrate


# Database Object

db = SQLAlchemy()


# Login Manager Object

login_manager = LoginManager()


# Migration Object

migrate = Migrate()


# Application Factory

def create_app():

    """
    Create Flask Application
    """

    # Root Directory

    BASE_DIR = Path(__file__).resolve().parent.parent

    # Create Flask App

    app = Flask(

        __name__,

        template_folder=str(
            BASE_DIR / "templates"
        ),

        static_folder=str(
            BASE_DIR / "app" / "static"
        )

    )

    # Load Configuration

    app.config.from_object(
        "config.Config"
    )

    # Initialize Extensions

    db.init_app(app)

    login_manager.init_app(app)

    migrate.init_app(app, db)

    # Login Page

    login_manager.login_view = "auth.login"

    login_manager.login_message_category = "warning"

    # Import Blueprints

    from app.main.routes import main

    from app.auth.routes import auth

    from app.posts.routes import posts

    from app.comments.routes import comments

    # Register Blueprints

    app.register_blueprint(main)

    app.register_blueprint(auth)

    app.register_blueprint(posts)

    app.register_blueprint(comments)

    # Return App

    return app