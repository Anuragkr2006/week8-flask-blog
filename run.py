"""
Application Entry Point
-----------------------
This file starts the Flask application.
"""

# Import Application Factory

from app import create_app


# Create Flask App

app = create_app()


# Run Application

if __name__ == "__main__":

    app.run(
        debug=True
    )