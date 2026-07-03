"""
Authentication Routes
---------------------
This file contains all authentication
related routes.
"""

# Import Required Modules

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from app import db
from app.models import User

from app.auth.forms import (
    RegisterForm,
    LoginForm
)


# Authentication Blueprint

auth = Blueprint(
    "auth",
    __name__
)


# ---------------------------------
# Register
# ---------------------------------

@auth.route("/register", methods=["GET", "POST"])
def register():

    # Redirect if already logged in

    if current_user.is_authenticated:

        return redirect(
            url_for("main.home")
        )

    form = RegisterForm()

    if form.validate_on_submit():

        # Check Email

        email = User.query.filter_by(
            email=form.email.data
        ).first()

        if email:

            flash(
                "Email already registered.",
                "danger"
            )

            return redirect(
                url_for("auth.register")
            )

        # Check Username

        username = User.query.filter_by(
            username=form.username.data
        ).first()

        if username:

            flash(
                "Username already exists.",
                "danger"
            )

            return redirect(
                url_for("auth.register")
            )

        # Create User

        user = User(

            username=form.username.data,

            email=form.email.data

        )

        # Hash Password

        user.set_password(
            form.password.data
        )

        # Save User

        db.session.add(user)

        db.session.commit()

        flash(

            "Registration successful. Please login.",

            "success"

        )

        return redirect(

            url_for("auth.login")

        )

    return render_template(

        "auth/register.html",

        title="Register",

        form=form

    )


# ---------------------------------
# Login
# ---------------------------------

@auth.route("/login", methods=["GET", "POST"])
def login():

    # Redirect if already logged in

    if current_user.is_authenticated:

        return redirect(
            url_for("main.home")
        )

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(

            email=form.email.data

        ).first()

        if user and user.check_password(

                form.password.data):

            login_user(user)

            flash(

                f"Welcome back, {user.username}!",

                "success"

            )

            return redirect(

                url_for("main.home")

            )

        flash(

            "Invalid email or password.",

            "danger"

        )

    return render_template(

        "auth/login.html",

        title="Login",

        form=form

    )


# ---------------------------------
# Logout
# ---------------------------------

@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash(

        "Logged out successfully.",

        "info"

    )

    return redirect(

        url_for("main.home")

    )