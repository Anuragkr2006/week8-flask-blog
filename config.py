"""
Application Configuration
-------------------------
This file contains all configuration settings
used by the Flask application.
"""

# Import OS Module

import os


# Base Project Directory

BASE_DIR = os.path.abspath(
    os.path.dirname(__file__)
)


# Configuration Class

class Config:
    """
    Flask Configuration Class
    """

    # Secret Key

    SECRET_KEY = "flask-blog-secret-key"

    # SQLite Database

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" +
        os.path.join(
            BASE_DIR,
            "instance",
            "blog.db"
        )
    )

    # Disable Modification Tracking

    SQLALCHEMY_TRACK_MODIFICATIONS = False