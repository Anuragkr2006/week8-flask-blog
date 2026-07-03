"""
Authentication Forms
--------------------
This file contains all forms related
to user registration and login.
"""

# Import FlaskForm

from flask_wtf import FlaskForm

# Import Form Fields

from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField

# Import Validators

from wtforms.validators import (
    DataRequired,
    Email,
    Length
)


# ----------------------------
# Registration Form
# ----------------------------

class RegisterForm(FlaskForm):

    # Username

    username = StringField(

        "Username",

        validators=[

            DataRequired(),

            Length(
                min=3,
                max=30
            )

        ]

    )

    # Email

    email = StringField(

        "Email",

        validators=[

            DataRequired(),

            Email()

        ]

    )

    # Password

    password = PasswordField(

        "Password",

        validators=[

            DataRequired(),

            Length(
                min=6
            )

        ]

    )

    # Register Button

    submit = SubmitField(

        "Register"

    )


# ----------------------------
# Login Form
# ----------------------------

class LoginForm(FlaskForm):

    # Email

    email = StringField(

        "Email",

        validators=[

            DataRequired(),

            Email()

        ]

    )

    # Password

    password = PasswordField(

        "Password",

        validators=[

            DataRequired()

        ]

    )

    # Login Button

    submit = SubmitField(

        "Login"

    )