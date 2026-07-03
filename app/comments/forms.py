"""
Comment Forms
-------------
This file contains all forms related
to blog comments.
"""

# Import FlaskForm

from flask_wtf import FlaskForm

# Import Form Fields

from wtforms import (
    TextAreaField,
    SubmitField
)

# Import Validators

from wtforms.validators import (
    DataRequired,
    Length
)


# ---------------------------------
# Comment Form
# ---------------------------------

class CommentForm(FlaskForm):

    # Comment

    comment = TextAreaField(

        "Write a Comment",

        validators=[

            DataRequired(),

            Length(
                min=2,
                max=1000
            )

        ]

    )

    # Submit Button

    submit = SubmitField(

        "Post Comment"

    )