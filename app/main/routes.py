"""
Main Routes
-----------
This file contains all routes related
to the main pages of the application.
"""

# Import Required Modules

from flask import (
    Blueprint,
    render_template
)

from flask_login import (
    login_required,
    current_user
)


# Create Main Blueprint

main = Blueprint(
    "main",
    __name__
)


# ---------------------------------
# Home Page
# ---------------------------------

@main.route("/")
def home():

    return render_template(

        "main/home.html",

        title="Home"

    )


# ---------------------------------
# About Page
# ---------------------------------

@main.route("/about")
def about():

    return render_template(

        "main/about.html",

        title="About"

    )


# ---------------------------------
# Profile Page
# ---------------------------------

@main.route("/profile")
@login_required
def profile():

    return render_template(

        "main/profile.html",

        title="My Profile",

        user=current_user

    )